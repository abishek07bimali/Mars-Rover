from django.shortcuts import render
from django.http import HttpResponse
import requests
import plotly.graph_objects as go
from django.core.paginator import Paginator
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive mode
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime
import time
import subprocess

# from home.models import Data

def dashboard(request):
    return render(request, 'dashboard.html')

def control(request):
    return render(request, 'control.html')


def map(request):
    return render(request, 'location.html')

def visualization(request):
    API_URL = f'https://api.thingspeak.com/channels/2163202/feeds.json?api_key=4U7LW3KAUDIO0SSF'

    response = requests.get(API_URL)
    data = response.json()['feeds']
    
    start_index = 80;
    end_index = 100;
    
    sliced_data = data[start_index:end_index]

    paginator = Paginator(sliced_data, 10)   # Display 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Generate the chart
    x = [entry['created_at'] for entry in sliced_data]
    y = [entry['field1'] for entry in sliced_data]
    x_formatted = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d") for date in x]


    fig, ax = plt.subplots()
    ax.plot(x_formatted, y)
    ax.set_xlabel('Date and Time')
    ax.set_ylabel('Value')
    ax.set_title('Data Chart')
    ax.tick_params(axis='x', rotation=90)
    plt.tight_layout()
    

    # Save chart image to a buffer
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    plt.close(fig)

    # Return the rendered template with the data and chart
    return render(request, 'visualization.html', {'page_obj': page_obj, 'chart': image_base64})


def run_script(request):
    if request.method == 'POST':
        # Execute the Python script
        subprocess.run(['python', 'C:/Users/ACER/Desktop/project/Mars-Rover/web/MarsRober/template/controller.py'])
    
    return render(request, 'control.html')
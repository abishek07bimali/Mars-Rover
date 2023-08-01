from django.shortcuts import render
import requests
from django.core.paginator import Paginator
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive mode
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime
import subprocess
import os

# from home.models import Data

def dash(request):
    url = f'https://api.thingspeak.com/channels/2182971/feeds.json?api_key=DK2ERBUX2LK9G0J2'
    res = requests.get(url)
    data = res.json()['feeds']
    # Extract the values for each field
    smoke = [float(entry['field6']) for entry in data]
    temp = [float(entry['field4']) for entry in data]
    humidity = [float(entry['field7']) for entry in data]

    # Calculate average, maximum, and minimum values for each field
    avg_smoke = sum(smoke) // len(smoke) if smoke else None
    max_smoke = max(smoke) if smoke else None
    min_smoke = min(smoke) if smoke else None

    avg_temp = sum(temp) //len(temp) if temp else None
    max_temp = max(temp) if temp else None
    min_temp = min(temp) if temp else None

    avg_humidity = sum(humidity) // len(humidity) if humidity else None
    max_humidity = max(humidity) if humidity else None
    min_humidity = min(humidity) if humidity else None

    return render(request, 'Dash.html', {
        'avg_smoke': avg_smoke,
        'max_smoke': max_smoke,
        'min_smoke': min_smoke,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'avg_humidity': avg_humidity,
        'max_humidity': max_humidity,
        'min_humidity': min_humidity,
    })

def dashboard(request):
    return render(request, 'dashboard.html')

def control(request):
    return render(request, 'control.html')

# field 7 ==> humidity
# field 6 ==> smoke
# field 4 ==> temperature


def visualization(request):
    API_URL = f'https://api.thingspeak.com/channels/2182971/feeds.json?api_key=DK2ERBUX2LK9G0J2'

    response = requests.get(API_URL)
    data = response.json()['feeds']

    latest_index = len(data)
    start_index = max(0, latest_index - 100)  
    end_index = latest_index  

    sliced_data = data[start_index:end_index]
    paginator = Paginator(sliced_data, 10)   # 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #chart for field1
    x_field1 = [entry['created_at'] for entry in sliced_data]
    y_field1 = [entry['field4'] for entry in sliced_data]
    # x_formatted_field1 = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d") for date in x_field1]

    fig_field1, ax_field1 = plt.subplots()
    ax_field1.plot(x_field1, y_field1)
    ax_field1.set_xlabel('Date')
    ax_field1.set_ylabel('Value')
    ax_field1.set_title('Data Chart for Field 1')
    ax_field1.tick_params(axis='x', rotation=45)
    plt.tight_layout()

    buffer_field1 = BytesIO()
    plt.savefig(buffer_field1, format='png')
    buffer_field1.seek(0)
    image_base64_field1 = base64.b64encode(buffer_field1.read()).decode('utf-8')

    plt.close(fig_field1)

    #chart for field2
    x_field2 = [entry['created_at'] for entry in sliced_data]
    y_field2 = [entry['field6'] for entry in sliced_data]
    # x_formatted_field2 = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d") for date in x_field2]

    fig_field2, ax_field2 = plt.subplots()
    ax_field2.plot(x_field2, y_field2)
    ax_field2.set_xlabel('Date')
    ax_field2.set_ylabel('Value')
    ax_field2.set_title('Data Chart for Field 2')
    ax_field2.tick_params(axis='x', rotation=45) 
    plt.tight_layout()

    buffer_field2 = BytesIO()
    plt.savefig(buffer_field2, format='png')
    buffer_field2.seek(0)
    image_base64_field2 = base64.b64encode(buffer_field2.read()).decode('utf-8')

    plt.close(fig_field2)

    # chart for field3
    x_field3 = [entry['created_at'] for entry in sliced_data]
    y_field3 = [entry['field7'] for entry in sliced_data]
    # x_formatted_field3 = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d") for date in x_field3]

    fig_field3, ax_field3 = plt.subplots()
    ax_field3.plot(x_field3, y_field3)
    ax_field3.set_xlabel('Date')
    ax_field3.set_ylabel('Value')
    ax_field3.set_title('Data Chart for Field 3')
    ax_field3.tick_params(axis='x', rotation=45) 
    plt.tight_layout()

    buffer_field3 = BytesIO()
    plt.savefig(buffer_field3, format='png')
    buffer_field3.seek(0)
    image_base64_field3 = base64.b64encode(buffer_field3.read()).decode('utf-8')

    plt.close(fig_field3)

    return render(request, 'visualization.html', {
        'page_obj': page_obj,
        'chart_field1': image_base64_field1,
        'chart_field2': image_base64_field2,
        'chart_field3': image_base64_field3,
    })

def map(request):
    # API_URL = f'https://api.thingspeak.com/channels/2182971/feeds.json?api_key=DK2ERBUX2LK9G0J2'

    # response = requests.get(API_URL)
    # data = response.json()['feeds']

    # last_entry = data[-1]
    # map_image_url = last_entry['field8']

    return render(request, 'location.html' )
    # , {'map_image_url': map_image_url}

def run_script(request):
    if request.method == 'POST':
        subprocess.run(['python', 'D:/Softwarica/SEM4/MarsRover/MarsRober/template/controller.py'])
    
    return render(request, 'control.html')


def display_images(request):
    # path to the folder (images)
    image_folder = 'D:/Softwarica/SEM4/MarsRover/MarsRober/static/images/' 

    # list of all the image filenames in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Generate the URLs for the images
    image_urls = [f'/media/{image}' for image in image_files]
    context = {'image_urls': image_urls}
    return render(request, 'images.html', context)
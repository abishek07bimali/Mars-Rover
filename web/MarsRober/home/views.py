from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import SignIn
from django.contrib import messages
import requests
from django.shortcuts import render
import plotly.graph_objects as go
from django.http import StreamingHttpResponse
import cv2


# Create your views here.

# def index(request):
#     context = {
#         "variable1":"this is sent",
#         "variable2":"this is not sent"
#     }
#     return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

# def video_feed(request):
#     return StreamingHttpResponse( content_type='multipart/x-mixed-replace; boundary=frame')


# def signIn(request):
#     if request.method=="POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         password = request.POST.get('password')
#         signIn = SignIn(name=name, email=email, password=password, address=address);
#         signIn.save()
#     messages.success(request, "Your account has been created.") 
#     return render(request, 'signIn.html')

def control(request):
    return render(request, 'control.html')

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         number = request.POST.get('number')
#         address = request.POST.get('address')
#         contact = Contact(name=name, email=email, number=number, address=address);
#         contact.save()
#     return render(request, 'contact.html')

def map(request):
    return render(request, 'location.html')

# gsbvm$HKR6hj9?f


import time

def visualization(request):
    url = "https://api.thingspeak.com/channels/2163202/feeds.json?api_key=4U7LW3KAUDIO0SSF"

    while True:
        print("normal")
        response = requests.get(url)
        data = response.json()
        feeds = data['feeds']

        # Extract data for visualization
        field1_values = []
        timestamps = []

        for feed in feeds:
            try:
                field1_value = float(feed['field1'])
                timestamp = feed['created_at']

                # Skip empty or invalid values
                if field1_value:
                    field1_values.append(field1_value)
                    timestamps.append(timestamp)
            except (ValueError, KeyError):
                # Handle empty or invalid values
                continue

        # Create the line chart trace for Field 1
        trace = go.Scatter(
            x=timestamps,
            y=field1_values,
            mode='lines',
            name='Field 1'
        )

        # Create the chart layout
        layout = go.Layout(
            title='ThingSpeak Data',
            xaxis=dict(title='Timestamp'),
            yaxis=dict(title='Value'),
            showlegend=True
        )

        # Create the chart figure
        fig = go.Figure(data=[trace], layout=layout)

        # Convert the chart to HTML
        chart_html = fig.to_html(full_html=False)

        context = {'feeds': feeds, 'chart_html': chart_html}
        return render(request, 'visualization.html', context)

        # Sleep for 10 seconds
        time.sleep(10)



    # for feed in feeds:
    #     if 'field1' in feed:
    #         field1_values.append(float(feed['field1']))
    #     timestamps.append(feed['created_at'])
    
    



# classNames = []
# classFile = "/home/pi/Desktop/Object_Detection_Files/coco.names"
# with open(classFile, "rt") as f:
#     classNames = f.read().rstrip("\n").split("\n")

# configPath = "/home/pi/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
# weightsPath = "/home/pi/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

# net = cv2.dnn_DetectionModel(weightsPath, configPath)
# net.setInputSize(320, 320)
# net.setInputScale(1.0 / 127.5)
# net.setInputMean((127.5, 127.5, 127.5))
# net.setInputSwapRB(True)


# def get_objects(img, thres, nms, draw=True, objects=[]):
#     classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
#     if len(objects) == 0:
#         objects = classNames
#     objectInfo = []
#     if len(classIds) != 0:
#         for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
#             className = classNames[classId - 1]
#             if className in objects:
#                 objectInfo.append([box, className])
#                 if draw:
#                     cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
#                     cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
#                                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
#                     cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
#                                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

#     return img, objectInfo


# def generate_video():
#     camera = cv2.VideoCapture(0)  # Adjust the camera index if necessary
#     while True:
#         ret, frame = camera.read()
#         if not ret:
#             break

#         frame, _ = get_objects(frame, 0.6, 0.2)
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def index(request):
    return render(request, 'index.html')


# def video_feed(request):
#     return StreamingHttpResponse(generate_video(), content_type='multipart/x-mixed-replace; boundary=frame')
import cv2
import os

# Load the object detection model and set the configuration
classNames = []
classFile = "/home/pi/Desktop/Object_Detection_Files/coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/pi/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/pi/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output_folder = "videos"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "person_video.avi")
    video_writer = None
    recording_start_time = None
    recording_duration = 4  # 4 seconds
    
    while True:
        success, img = cap.read()

        # Object detection code
        classIds, confs, bbox = net.detect(img, confThreshold=0.6, nmsThreshold=0.2)

        person_detected = False
        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                className = classNames[classId - 1]
                if className == 'person':
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, className.upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    
                    person_detected = True

        # Start recording if a person is detected
        if person_detected and video_writer is None:
            video_writer = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))
            recording_start_time = cv2.getTickCount()

        # Stop recording if the recording duration is reached
        if video_writer is not None and (cv2.getTickCount() - recording_start_time) / cv2.getTickFrequency() >= recording_duration:
            video_writer.release()
            video_writer = None

        # Write the frame to the video file
        if video_writer is not None:
            video_writer.write(img)

        cv2.imshow("Output", img)
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video writer and capture device
    if video_writer is not None:
        video_writer.release()
    cap.release()
    cv2.destroyAllWindows()

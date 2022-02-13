# Containers, Kubernetes, and IoT Edge
The objective of this project is to build a lightweight containerized application pipeline with components running on the edge, a Jetson NX, and in the cloud, a VM in AWS. The application will capture faces from a webcam video stream and transmit the images via MQTT to and AWS S3 bucket

## Repository Structure

john-andrus-w251-hw3  
+- 1-jetson-logger  
|---- Dockerfile  
|---- detector-deployment.yaml  
|---- detector.py  
|---- haarcascade_frontalface_default.xml  
+- 2-jetson-broker  
|---- Dockerfile  
|---- broker-deployment.yaml  
|---- broker-service.yaml  
+- 3-jetson-forwarder  
|---- Dockerfile  
|---- forwarder-deployment.yaml  
|---- forwarder.py  
+- 3-jetson-logger  
|---- Dockerfile  
|---- logger-deployment.yaml  
+- 4-cloud-broker  
|---- Dockerfile  
+- 5-cloud-processor  
|---- Dockerfile  
|---- processor.py  
+- 6-s3-object-storage  
|---- s3.md  
|---- screenshot.png  
  

## MQTT Topics and QoS
I chose to call the MQTT topic cam/face in order to tie the topic to a specific application (face detection) and a specific edge device (webcam). Even though this project only uses a single edge device for a single application, this naming scheme allows for scaling and meets the MQTT topic naming best practices.

I chose a QoS of 0 ("at most once") because this project is a proof of concept that captures many images of an individual's face. Little if any value is lost if some of these images are lost, so I opted to prioritize time efficiency.
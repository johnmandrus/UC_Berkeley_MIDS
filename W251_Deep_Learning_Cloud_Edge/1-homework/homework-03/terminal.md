# Start Kubernetes
sudo systemctl start k3s

# Install Mosquitto
sudo apt-get install mosquitto

#Create the Jetson Deployment
kubectl apply -f dbf-deployment.yaml

#Create the Jetson Service
kubectl apply -f dbf-service.yaml
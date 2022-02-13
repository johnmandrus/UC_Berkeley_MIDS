FROM alpine:latest
RUN apk add mosquitto
RUN apk add -y python3-dev python3-pip python3-opencv
RUN pip3 install Cython
RUN pip3 install numpy
COPY forwarder.py forwarder.py
CMD ["python3", "forwarder.py"]
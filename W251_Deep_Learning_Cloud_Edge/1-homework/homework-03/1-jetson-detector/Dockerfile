FROM ubuntu:latest
RUN apt-get update
RUN apt install -y python3-dev python3-pip python3-opencv
RUN pip3 install Cython
RUN pip3 install numpy
COPY detector.py detector.py
CMD ["python3", "detector.py"]

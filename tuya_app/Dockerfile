# Use the official Alpine image as the base
FROM alpine:latest

# Install necessary packages
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    linux-headers \
    opencv-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libwebp-dev

# Install OpenCV Python bindings
RUN pip3 install numpy opencv-python paho-mqtt

# Set the working directory
WORKDIR /app

# Copy your application files into the container
COPY . /app

# Install Python dependencies, including opencv-python
RUN pip3 install --no-cache-dir \
    opencv-python \
    numpy

# Expose any necessary ports (if your app uses them)
# EXPOSE 5000  # Example: exposing port 5000 for Flask app

# Set the default command to run your application
# CMD ["./tuya_app_start.sh"]

RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir img

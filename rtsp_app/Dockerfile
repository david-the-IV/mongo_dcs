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
    libwebp-dev \
    openssh \
    sudo \
    bash \
    && mkdir /var/run/sshd \
    && ssh-keygen -A

# Add users with their passwords
RUN adduser -D edy && echo "edy:20edy25" | chpasswd
RUN adduser -D ridho && echo "ridho:20ridho25" | chpasswd

# Allow users to login via SSH
RUN echo "edy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && echo "ridho ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Expose SSH ports 2223 for rtsp_app
EXPOSE 2223

# Start the SSH daemon on port 2223
CMD /usr/sbin/sshd -D -p 2223

# Set the working directory
WORKDIR /app

# Install OpenCV Python bindings and MQTT
RUN pip3 install --no-cache-dir \
    numpy \
    opencv-python \
    paho-mqtt

# Copy your application files into the container
COPY . /app

# Expose any necessary ports (if your app uses them)
# EXPOSE 5000  # Example: exposing port 5000 for Flask app

# Set the default command to run your application
# CMD sh -c "ipcam.py && ipcam_no-windows.py && mqtt2rtsp.py"
RUN chmod +x ./rtsp_app_start.sh
CMD ["./rtsp_app_start.sh"]

# RUN pip3 install --no-cache-dir -r requirements.txt
# RUN git clone https://github.com/MR12b/TIK-projekt.git
RUN mkdir -p /app/img

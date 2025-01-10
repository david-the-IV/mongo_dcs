# Use the official Alpine image as the base
FROM alpine:latest

# Install necessary packages
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    linux-headers \
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

# Expose SSH port 2224 for tuya_app
EXPOSE 2224

# Start the SSH daemon on port 2224
CMD /usr/sbin/sshd -D -p 2224

# Set the working directory
WORKDIR /app

# Install Python dependencies for Tuya API and MQTT
RUN pip3 install --no-cache-dir \
    tuya-iot-py-sdk \
    paho-mqtt

# Copy your application files into the container
COPY . /app

# Ensure the startup script is executable
RUN chmod +x ./tuya_app_start.sh

# Set the default command to run your Tuya application
CMD ["./tuya_app_start.sh"]

# Create a directory for storing images or logs if needed
RUN mkdir -p /app/img

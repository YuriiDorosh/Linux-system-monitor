# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the maintainer label
LABEL maintainer="yuriydorosh2005@gmail.com"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg scrot git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /usr/src/app

# Clone the repository
RUN git clone https://github.com/YuriiDorosh/Linux-system-monitor.git .

# Set up a virtual environment
RUN python -m venv env

# Activate the virtual environment
ENV PATH="/usr/src/app/env/bin:$PATH"

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your application using CMD which keeps the container running.
CMD ["python3", "src/main.py"]

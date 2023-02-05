# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the calculator script to the container
COPY calculator.py .

# Install the required packages
RUN pip install --no-cache-dir Flask

# Set the environment variable for Flask
ENV FLASK_APP=calculator.py

# Expose port 5000 to allow external traffic to access the app
EXPOSE 5000

# Set the entrypoint to run the Flask application
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

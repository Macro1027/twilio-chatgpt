# Use the official Python image as the base image
FROM python:3.10.3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Flask application code into the container
COPY . /app

# Expose port 5000 for the Flask application
EXPOSE 8080

ENV PORT 8080

# Start ngrok and the Flask application when the container starts

CMD python run.py 
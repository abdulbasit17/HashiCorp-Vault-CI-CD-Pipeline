# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV VAULT_ADDR=http://127.0.0.1:8200

# Run app.py when the container launches
CMD ["python3", "app.py"]

# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Set the FLASK_APP environment variable
ENV FLASK_APP=src.app:app

# Set the entrypoint command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

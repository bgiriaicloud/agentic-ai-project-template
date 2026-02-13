# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/agentic_ai_project
# We copy to a subdirectory to match the module import structure (import agentic_ai_project.workflows...)
COPY . /app/agentic_ai_project

# Set environment variable for Python path to include the /app directory
ENV PYTHONPATH="/app"

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run api.py via uvicorn when the container launches
CMD ["uvicorn", "agentic_ai_project.api:app", "--host", "0.0.0.0", "--port", "8080"]

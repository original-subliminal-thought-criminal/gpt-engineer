# Start from the Python 3.11.4 base image
FROM python:3.11.4-slim-bookworm

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements.txt file into our workdir
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install -U Flask

# Copy the rest of our application's source code into the workdir
COPY . .

# Set environment variables in Docker
ENV OPENAI_API_KEY your_api_key_here
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port flask is going to run on
EXPOSE 5000

# Create a volume for persistent data
VOLUME [ "/app/my-new-project/workspace" ]

# The command to run our application when the Docker container starts
CMD [ "flask", "run" ]
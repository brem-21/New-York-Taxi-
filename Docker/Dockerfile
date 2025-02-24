# Use the official Python 3.12.8 image
FROM python:3.12.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to /app
COPY requirements.txt requirements.txt

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY ingest_data.py ingest_data.py

# Define the entrypoint to run the Python script
ENTRYPOINT ["python3", "ingest_data.py"]

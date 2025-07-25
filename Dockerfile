# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application script into the container
COPY app.py .

# Expose the port the app runs on
EXPOSE 7860

# Command to run the app when the container launches
CMD ["python", "app.py"]
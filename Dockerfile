# Use official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

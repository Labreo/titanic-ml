# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt if you have one
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .


# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
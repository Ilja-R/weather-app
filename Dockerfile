# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies (from requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "src/app.py"]
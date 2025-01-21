# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the text file with the test score-table
COPY test.txt /app/test.txt
# Expose the port that the Flask app runs on
EXPOSE 8777

# Set environment variables
ENV FLASK_APP=MainGame.py
ENV FLASK_ENV=production

# Run the application
CMD ["python3", "MainGame.py"]






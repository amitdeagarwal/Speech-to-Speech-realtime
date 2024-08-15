# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port and run the application
EXPOSE 5000

# Use Gunicorn to run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

# Dockerfile (optional).
# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for pyodbc if needed, optional)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder
COPY app ./app

# Expose port
EXPOSE 8080

# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

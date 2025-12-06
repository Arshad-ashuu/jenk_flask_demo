# Dockerfile

# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system deps (optional but useful)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#  && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Use gunicorn in container (better than flask dev server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

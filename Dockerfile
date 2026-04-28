FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (optional but useful)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Run tests by default
CMD ["pytest", "-v", "--alluredir=allure-results"]
# Use official slim Python base image

FROM python:3.12-slim



# Set working directory

WORKDIR /app



# Install required system dependencies including CA certs

RUN apt-get update && apt-get install -y \

    build-essential \

    ca-certificates \

    curl \

    && update-ca-certificates \

    && rm -rf /var/lib/apt/lists/*



# Ensure certifi is used for SSL certificates

ENV SSL_CERT_FILE=/usr/local/lib/python3.12/site-packages/certifi/cacert.pem



# Copy requirements first (for better Docker cache usage)

COPY requirements.txt .



# Install pip/setuptools/wheel with SSL verification disabled for PyPI

RUN pip install --no-cache-dir -r requirements.txt \

    --trusted-host pypi.org \

    --trusted-host files.pythonhosted.org \

    --trusted-host pypi.python.org \

    --timeout=120 \

    --retries=10 \

    --prefer-binary \

    --progress-bar=off



# Copy app code

COPY . .



ENV GRADIO_SERVER_NAME=0.0.0.0

ENV GRADIO_SERVER_PORT=7860



# Run app

CMD ["python", "agent.py"]


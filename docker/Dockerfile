FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    bash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY scripts/ scripts/
COPY assets/ assets/

RUN pip install --no-cache-dir \
    google-api-python-client \
    google-auth-httplib2 \
    google-auth-oauthlib

CMD ["sleep", "infinity"]

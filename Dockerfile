FROM python:3.11-slim

WORKDIR /app

# Install git for cloning private repos
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Declare ARG for GitHub token - Railway passes matching env vars automatically
ARG GITHUB_TOKEN

# Configure git to use the token and install private package
RUN git config --global url."https://${GITHUB_TOKEN}@github.com/".insteadOf "https://github.com/" && \
    pip install --no-cache-dir git+https://github.com/ai-emerald/emerald-component-library.git

# Copy application code
COPY . .

# Railway provides PORT env var
ENV PORT=8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

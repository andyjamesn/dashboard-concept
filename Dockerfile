FROM python:3.11-slim

WORKDIR /app

# Install git for cloning private repos
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Declare ARG for GitHub token
ARG GITHUB_TOKEN

# Debug: Check if token is passed (will show length, not value)
RUN echo "Token length: ${#GITHUB_TOKEN}"

# Disable git credential prompts and install private package
ENV GIT_TERMINAL_PROMPT=0
ENV GIT_ASKPASS=/bin/true
RUN pip install --no-cache-dir "git+https://${GITHUB_TOKEN}@github.com/ai-emerald/emerald-component-library.git"

# Copy application code
COPY . .

# Railway provides PORT env var
ENV PORT=8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

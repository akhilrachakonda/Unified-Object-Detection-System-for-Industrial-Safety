FROM python:3.9-slim

WORKDIR /app

# Copy requirements first (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install FastAPI + Uvicorn (for serving)
RUN pip install fastapi uvicorn[standard] ultralytics

# Copy all project files
COPY . .

EXPOSE 5000

# Start FastAPI server when container runs
CMD ["uvicorn", "inference_server:app", "--host", "0.0.0.0", "--port", "5000"]

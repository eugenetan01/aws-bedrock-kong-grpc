# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables to prevent buffer issues
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app
WORKDIR /app

# Expose the required port for Streamlit (if running locally or via Docker)
EXPOSE 8501

# Command to run the Streamlit app when container starts
CMD ["streamlit", "run", "ui.py", "--server.port", "8501", "--server.address=0.0.0.0"]

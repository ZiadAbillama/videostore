# ---- 1. Use an official lightweight Python image ----
FROM python:3.11-slim

# ---- 2. Set environment variables ----
# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- 3. Set working directory inside container ----
WORKDIR /app

# ---- 4. Install system dependencies (optional but useful) ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# ---- 5. Copy and install Python dependencies ----
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ---- 6. Copy the rest of the project code ----
COPY . /app/

# ---- 7. Expose port 8000 (default Django dev server port) ----
EXPOSE 8000

# ---- 8. Start Django development server ----
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 

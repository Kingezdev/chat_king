# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /core

# Install dependencies
COPY requirements.txt /core/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /core/

# Expose port 8000
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

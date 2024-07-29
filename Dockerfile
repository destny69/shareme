# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# Add entrypoint script
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

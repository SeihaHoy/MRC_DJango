# syntax=docker/dockerfile:1.4

FROM python:3.9

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mysite.settings

# Set the working directory to /app
WORKDIR /app

# Copy the application code and the script
COPY . /app
COPY start_servers.sh /app/

# Ensure the script has execute permissions
# RUN chmod +x /app/start_servers.sh
RUN ["chmod", "+x", "/app/start_servers.sh"]

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["sh","/app/start_servers.sh"]
FROM python:3.9-slim

# Copy the application code into the container
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir requests Flask

# Expose the port that Flask will run on (5000 by default)
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "./app.py"]

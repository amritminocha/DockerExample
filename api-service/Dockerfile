FROM python:3.10-slim-bullseye

COPY requirements.txt requirements.txt

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt

# install app
COPY app.py /

# final configuration
EXPOSE 80
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8085"]
FROM ubuntu:latest

# Update the ubuntu image
RUN apt-get update -y

# Install the requirements
RUN apt-get install -y python3 python3-pip python3-dev build-essential

# Copy needed files in the container
COPY ./requirements.txt /usr/src/app/
COPY ./app.py /usr/src/app/
# Install python requirements
RUN pip3 install -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]

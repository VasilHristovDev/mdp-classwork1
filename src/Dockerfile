FROM alpine:latest

# Update the ubuntu image
RUN apk update

# Install the requirements
RUN apk add python3 py3-pip py3-dev build-base

# Copy needed files in the container
COPY ./requirements.txt /usr/src/app/
COPY ./app.py /usr/src/app/
# Install python requirements
RUN pip3 install -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]

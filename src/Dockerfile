ARG COMMIT_SHA
FROM alpine:latest

LABEL commit_sha=$COMMIT_SHA
# Update the ubuntu image
RUN apk upgrade

# Install the requirements
RUN apk add python3 py3-pip python3-dev

# Add a nonroot user for regular operations
RUN addgroup -S nonroot
RUN adduser -S nonroot -G nonroot

# Use the non root user for regular operations
USER nonroot

# Copy needed files in the container
COPY ./requirements.txt /usr/src/app/
COPY ./app.py /usr/src/app/

# Install python requirements
RUN pip3 install -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]

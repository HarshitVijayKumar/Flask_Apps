FROM ubuntu:23.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
    WORKDIR /app
    COPY ./requirements.txt /app/requirements.txt
    RUN pip install -r requirements.txt --break-system-packages

    COPY . . 

    EXPOSE 5000

    CMD ["flask", "run", "--host=0.0.0.0"]
# Stage 1 - make build image
FROM python:3.10-buster AS builder

WORKDIR /backend-flask

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]



# Stage 2 - make production image 
FROM python:3.10-slim-buster

RUN apt-get -y update; apt-get -y install curl

WORKDIR /backend-flask

ENV FLASK_ENV=development
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /backend-flask .

EXPOSE ${PORT}

HEALTHCHECK CMD curl --fail http://localhost:4567/api/activities/home || exit 1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
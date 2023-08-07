FROM python:3.10

ARG OPENAI_API_KEY

ENV OPENAI_API_KEY=$OPENAI_API_KEY

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
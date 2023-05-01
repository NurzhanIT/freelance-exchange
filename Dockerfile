FROM python:3.9-alpine3.16

COPY /requirements.txt /temp/requirements.txt

COPY work_marketplace /work_marketplace

WORKDIR /work_marketplace

EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser  --disabled-password work_marketplace-user

USER work_marketplace-user

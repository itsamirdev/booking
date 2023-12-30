FROM python:3.13.0a1-slim-bullseye


WORKDIR /project

COPY requirements.txt /project/

RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "A.wsgi", ":8000"]

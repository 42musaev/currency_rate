FROM python:3.8

WORKDIR /backend

COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . .

EXPOSE 8000

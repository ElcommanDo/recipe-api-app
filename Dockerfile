FROM python: 3.7-alpine
MAINTAINER ElcommanDo
ENV PYTHONUNBUFFERED 1
COPY  ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPT ./app /app
RUN adduser -d user
USER user

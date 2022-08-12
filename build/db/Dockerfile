FROM mariadb:latest

RUN apt-get update
COPY ./db_actress.sql /docker-entrypoint-initdb.d/

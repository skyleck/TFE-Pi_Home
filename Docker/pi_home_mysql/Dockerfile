FROM debian:jessie

RUN apt-get update && apt-get upgrade

RUN echo "mysql-server mysql-server/root_password password password" \
	| debconf-set-selections

RUN echo "mysql-server mysql-server/root_password_again password password"\
	| debconf-set-selections

RUN mkdir /docker_entrypoint-initdb.d/
COPY ./sql-scripts/ /docker_entrypoint-initdb.d/

RUN  apt-get install -y  mysql-server

COPY ./docker-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306

CMD ["mysqld"]



FROM debian:stretch-slim

RUN apt-get -y update && apt-get -y upgrade

RUN echo "mysql-server mysql-server/root_password password password" \
	| debconf-set-selections

RUN echo "mysql-server mysql-server/root_password_again password password"\
	| debconf-set-selections

RUN mkdir /docker_entrypoint-initdb.d/
COPY ./sql-scripts/ /docker_entrypoint-initdb.d/

RUN  apt-get install -y  mysql-server

COPY ./docker-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/docker-entrypoint.sh

RUN service mysql start
#mysql -u root --password=password -e "CREATE DATABASE pi_home"
#RUN sed -i 's|/var/lib/mysql|/var/lib/mysql-data|g' /etc/mysql/mysql.conf.d/mysqld.cnf
RUN ./usr/bin/docker-entrypoint.sh

RUN service mysql restart
EXPOSE 3306

CMD ["mysqld"]



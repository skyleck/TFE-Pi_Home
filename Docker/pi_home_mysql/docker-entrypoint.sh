#!/bin/bash 
set -e

service mysql start

mysql -u root --password=password -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('"test"');"

mysql -u root --password="test" -e "CREATE DATABASE pi_home;"
mysql -u root --password="test" -e "CREATE DATABASE pi_home_test;"

for f in /docker_entrypoint-initdb.d/*; do
	sleep 5
	mysql -u root --password="test" < $f
done

sed -e "s/^bind-address\(.*\)=.*/bind-address=0.0.0.0/" -i /etc/mysql/mariadb.conf.d/50-server.cnf

mysql -u root --password="test" -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'test' WITH GRANT OPTION;"

exec "$@"

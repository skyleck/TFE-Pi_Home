#!/bin/bash 
set -e 

service mysql start

mysql -u root --password=password -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('"$MYSQL_ROOT_PASSWORD"');"

mysql -u root --password="$MYSQL_ROOT_PASSWORD" -e "CREATE DATABASE pi_home;"
mysql -u root --password="$MYSQL_ROOT_PASSWORD" -e "CREATE DATABASE pi_home_test;"

for f in /docker_entrypoint-initdb.d/*; do
	mysql -u root --password="$MYSQL_ROOT_PASSWORD" < $f
done

sed -e "s/^bind-address\(.*\)=.*/bind-address=0.0.0.0/" -i /etc/mysql/my.cnf
mysql -u root --password="$MYSQL_ROOT_PASSWORD" -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '"$MYSQL_ROOT_PASSWORD"' WITH GRANT OPTION; FLUSH PRIVILEGES;"

service mysql stop

exec "$@"

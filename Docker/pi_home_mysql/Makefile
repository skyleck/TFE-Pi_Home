DOCKER_IMAGE_NAME=pi_home_mysql

default: build

build:
	docker build -t "$(DOCKER_IMAGE_NAME)" .

test:
	docker run --rm $(DOCKER_IMAGE_NAME) --net host -e MYSQL_ROOT_PASSWORD=${password} -p 3306:3306 /bin/echo "Success."

version:
	docker run --rm $(DOCKER_IMAGE_NAME) mysql --version

rmi:
	docker rmi -f $(DOCKER_IMAGE_NAME)

run:
	docker run --name $(DOCKER_IMAGE_NAME) --net host -e MYSQL_ROOT_PASSWORD=$(password) -d -p 3306:3306 $(DOCKER_IMAGE_NAME)

stop:
	docker stop $(DOCKER_IMAGE_NAME)
	docker rm $(DOCKER_IMAGE_NAME)

rebuild: rmi build

rerun: stop run

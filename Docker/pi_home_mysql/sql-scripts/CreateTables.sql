USE pi_home;

CREATE TABLE `user` (
	id INTEGER AUTO_INCREMENT,
	login varchar(25) NOT NULL,
	firstname varchar(25) NOT NULL,
	lastname varchar(25) NOT NULL,
	password varchar(255) NOT NULL,
	authorization TINYINT NOT NULL,
	PRIMARY KEY(id)
);

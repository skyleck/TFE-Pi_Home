USE pi_home;

CREATE TABLE `user` (
	id INTEGER AUTO_INCREMENT,	
	firstname varchar(25) NOT NULL,
	lastname varchar(25) NOT NULL,
	password varchar(100) NOT NULL,
	PRIMARY KEY(id)
);

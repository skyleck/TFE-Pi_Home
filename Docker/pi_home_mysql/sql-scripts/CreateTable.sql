USE pi_home;

CREATE TABLE `user` (
	id INTEGER AUTO_INCREMENT,	
	first_name varchar(25) NOT NULL,
	last_name varchar(25) NOT NULL,
	password varchar(100) NOT NULL,
	PRIMARY KEY(id)
);

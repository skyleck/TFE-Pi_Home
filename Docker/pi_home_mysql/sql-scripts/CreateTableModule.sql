USE pi_home;

CREATE TABLE `module` (
	id INTEGER AUTO_INCREMENT,
	name varchar(100) NOT NULL,
	ip varchar(15) NOT NULL,
	state TINYINT(1) NOT NULL,
	PRIMARY KEY(id)
);

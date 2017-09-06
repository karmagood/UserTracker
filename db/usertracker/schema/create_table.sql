CREATE TABLE IF NOT EXISTS users (
	user_id int(10) NOT NULL AUTO_INCREMENT,
	username varchar(255) NOT NULL,
	email varchar(255),
	history_path varchar(255),
	PRIMARY KEY (user_id),
	KEY (username)
);
CREATE TABLE IF NOT EXISTS commands (
	command_id int(10) NOT NULL AUTO_INCREMENT,
	command varchar(255) NOT NULL,
	threshold integer,
	KEY(command),
	PRIMARY KEY (command_id)
);
CREATE TABLE IF NOT EXISTS user_command (
	user_id int(10) NOT NULL,
	command_id int(10) NOT NULL,
	counter int(10),
	PRIMARY KEY (user_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (command_id) REFERENCES commands(command_id)

);

		

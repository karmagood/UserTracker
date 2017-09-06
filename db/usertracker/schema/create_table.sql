CREATE TABLE IF NOT EXISTS users (
	username varchar(255) NOT NULL,
	email varchar(255),
	history_path varchar(255),
	PRIMARY KEY (username)
);
CREATE TABLE IF NOT EXISTS user_command (
	username varchar(255) NOT NULL,
	command varchar(255)  NOT NULL,
	CONSTRAINT PK_username_command PRIMARY KEY
	(
		username,
		command
	),
	FOREIGN KEY (username) REFERENCES users (username),
	FOREIGN KEY (command) REFERENCES commands (command), 
	counter int
);
CREATE TABLE IF NOT EXISTS commands (
	command varchar(255) NOT NULL,
	threshold integer,
	PRIMARY KEY (command)
);
	

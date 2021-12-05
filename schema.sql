CREATE TABLE comments (
   	id SERIAL PRIMARY KEY,
   	content TEXT,
	players_id INTEGER REFERENCES players,
	users_id INTEGER REFERENCES users
);

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
    	password TEXT
);
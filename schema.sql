CREATE TABLE Users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
    	password TEXT
);

CREATE TABLE Files (
	id SERIAL PRIMARY KEY,
	file_name TEXT,
	hidden BOOLEAN,
	created_at TIMESTAMP DEFAULT NOW(),
	user_id INTEGER REFERENCES Users	
);

CREATE TABLE players (
   	id SERIAL PRIMARY KEY,
	name TEXT,
	team TEXT,
	pos TEXT,
	games INTEGER,
	goals INTEGER,
	assists INTEGER,
	points INTEGER,
	plusminus INTEGER,
	penalty INTEGER,
	shots INTEGER,
	gwg INTEGER,
	ppg INTEGER,
	ppa INTEGER,
	shg INTEGER,
	sha INTEGER,
	hits INTEGER,
	blocked INTEGER,
	file_id INTEGER REFERENCES Files
);

CREATE TABLE Comments (
   	id SERIAL PRIMARY KEY,
   	content TEXT,
	created_at TIMESTAMP DEFAULT NOW(),
	players_id INTEGER REFERENCES Players,
	users_id INTEGER REFERENCES Users
	
);

CREATE TABLE PlayerLikes (
	id SERIAL PRIMARY KEY,
	likes BOOLEAN,
	player_id INTEGER REFERENCES Players,
	user_id INTEGER REFERENCES Users
);

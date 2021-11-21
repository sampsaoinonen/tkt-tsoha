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
	blocked INTEGER
);

CREATE TABLE comments (
   	id SERIAL PRIMARY KEY,
   	content TEXT,
	players_id INTEGER REFERENCES players
);

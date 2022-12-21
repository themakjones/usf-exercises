DROP DATABASE IF EXISTS soccer_league;

CREATE DATABASE soccer_league;

\c soccer_league;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name INTEGER NOT NULL
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    team_id INTEGER REFERENCES teams,
);

CREATE TABLE referees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team INTEGER REFERENCES teams
    away_team INTEGER REFERENCES teams
    season_id INTEGER REFERENCES seasons
);

CREATE TABLE assigned_refs (
    ref_id INTEGER REFERENCES referees,
    match_id INTEGER REFERENCES matches
);

CREATE TABLE goals (
    match_id INTEGER REFERENCES matches,
    player_id INTEGER REFERENCES players,
    match_time TIMESTAMP NOT NULL,
    own_goal BOOLEAN NOT NULL
);
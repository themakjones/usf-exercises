DROP DATABASE IF EXISTS craigslist;

CREATE DATABASE craigslist;

\c craigslist;

CREATE TABLE region (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(15) NOT NULL,
    preferred_region INTEGER REFERENCES region
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15),
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(25) NOT NULL,
    category_id INTEGER REFERENCES categories,
    user_id INTEGER REFERENCES users,
    content TEXT,
    region_id INTEGER REFERENCES region,
    location VARCHAR(15)
);

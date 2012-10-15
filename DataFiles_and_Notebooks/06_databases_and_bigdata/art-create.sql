-- art-create.sql
--    Make three tables in sqlite3 to hold artists, museums, and artwork
--     Created by J. S. Bloom for the UC Berkeley AY250 Fall 250 Python Seminar
--
CREATE TABLE museum (
mid INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT DEFAULT 0,
name TEXT,
country TEXT,
city TEXT);

CREATE TABLE artist (
aid integer  NOT NULL  PRIMARY KEY AUTOINCREMENT DEFAULT 0,
first_name     text,
last_name      text,
birth_date date  NOT NULL DEFAULT CURRENT_DATE,
birth_country   text,
death_date date
);

CREATE TABLE work (
wid INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT DEFAULT 0,
aid INTEGER  NOT NULL  DEFAULT 0,
title TEXT,
type TEXT,
mid integer,
finish_date Date);

--- For those who want to see a little more nitty gritty how how this DB would actually be set up...
--- 
--- if we had a lot of data, we'd want to tell sqlite3 that mid and aid in work should be indexed:
--- CREATE UNIQUE INDEX work_aid ON work(aid)
--- CREATE UNIQUE INDEX work_mid ON work(mid)
--- 
--- We'd also want to tell sqlite3 that mid and aid are foreign keys
--- CREATE TABLE work (
    -- wid INTEGER  NOT NULL  PRIMARY KEY AUTOINCREMENT DEFAULT 0,
    -- aid INTEGER  NOT NULL  DEFAULT 0,
    -- title TEXT,
    -- type TEXT,
    -- mid integer,
    -- finish_date Date,
    ---FOREIGN KEY (aid) REFERENCES artist(aid),
    ---FOREIGN KEY (mid) REFERENCES museum(mid));
----
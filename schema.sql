DROP TABLE IF EXISTS list;

CREATE TABLE list (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task TEXT UNIQUE NOT NULL,
  done BOOLEAN NOT NULL
);



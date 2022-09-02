-- ran this against the heroku db directly

CREATE TABLE IF NOT EXISTS ntee_codes(
  ID SERIAL PRIMARY KEY,
  code VARCHAR(256),
  name VARCHAR(256),
  definition TEXT   -- text has no character size limit
);

\copy ntee_codes (code, name, definition) FROM '/Users/lucaswiley/Desktop/nonprofits/ntee_codes.csv' CSV HEADER
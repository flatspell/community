-- ran this against the heroku db directly

CREATE TABLE IF NOT EXISTS nonprofits(
  ID SERIAL PRIMARY KEY,
  EIN INTEGER,
  STREIN VARCHAR(256),
  NAME VARCHAR(256),
  SUB_NAME VARCHAR(256),
  CITY VARCHAR(256),
  STATE VARCHAR(256),
  NTEE_CODE VARCHAR(256),
  RAW_NTEE_CODE VARCHAR(256),
  SUBSECCD INTEGER,
  HAS_SUBSECCD BOOLEAN,
  HAVE_FILINGS VARCHAR(256),
  HAVE_EXTRACTS VARCHAR(256),
  HAVE_PDFS VARCHAR(256),
  SCORE NUMERIC
);

\copy nonprofits (ein, strein, name, sub_name, city, state, ntee_code, raw_ntee_code, subseccd, has_subseccd, have_filings, have_extracts, have_pdfs, score) FROM '/Users/lucaswiley/Desktop/nonprofits/merged_csv/nonprofits_merged.csv' CSV HEADER
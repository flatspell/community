from sqlalchemy import create_engine

sql_query = (
		"""
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
		"""
)

def create_table():
	db_string = "postgresql://lucaswiley:localhost@localhost/flatspell"
	db = create_engine(db_string)

	# Create 
	db.execute(sql_query)

	# Read
	result_set = db.execute("SELECT * FROM nonprofits")  
	for r in result_set:  
			print(r)

if __name__ == '__main__':
	create_table()










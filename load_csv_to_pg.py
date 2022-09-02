import pandas as pd
import os

from sqlalchemy import create_engine

engine = create_engine('postgresql://lucaswiley:localhost@localhost/flatspell')


df = pd.read_csv('/Users/lucaswiley/Desktop/nonprofits/merged_csv/nonprofits_merged.csv')

conn = engine.connect()
df.to_sql('nonprofits', con=conn, if_exists='append', index=False)
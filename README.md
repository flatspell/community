# community

Right now it's just a script for extracting nonprofit data from propublica.org. Every other API charges for their data. I do get rate-limited by pro-publica so I'll need to look into a way to get more data from them or have the script sleep for 1 minute after every 60 records or so.

Merged csv of all Washington non-profits is stored locally on my machine. 

TODO:
- Move this data to heroku postgres.
- Figure out location data beyond city, zip code is probably ideal
- Either way, we'll need GEOs around each city/zip in order to coordinate against a user's request say based on shipping address

# community
Main repo for FlatSpell Technologies Community product.

Here's the white-paper: https://docs.google.com/document/d/17CWfyLtK_Xe6IuP9kkiat9gJ85Rz_Z0KaHwy5GWUasg/edit#

Right now it's just a script for extracting nonprofit data from propublica.org. Every other API charges $ for their data. I do get rate-limited by pro-publica so I'll need to look into a way to get more data from them or have the script sleep for 1 minute after every 60 records or so.

Merged csv of all Washington non-profits is stored locally on my machine. 

TODO:
- Find a way to extract more records. [ProPublica](https://projects.propublica.org/nonprofits/search?utf8=%E2%9C%93&q=port+angeles&state%5Bid%5D=&ntee%5Bid%5D=&c_code%5Bid%5D=) show 304 organizations for "Port Angeles" but looks like you only have ~60-70 in your data. 
- Figure out location data beyond city, zip code is probably ideal
- Either way, we'll need GEOs around each city/zip in order to coordinate against a user's request say based on shipping address
- Eventually we'll want to pull this data from Guidestar, but I'd like to have enough revenue to validate the $2-5K/year cost for the api subscription. Make do with pro publica in the meantime.

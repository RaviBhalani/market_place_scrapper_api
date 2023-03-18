# market_place_scrapper_api

**Steps to run the project:**
1. Take clone of the master branch of the project.
2. Install requirements: pip install -r requirements.txt.
3. Run the server: python manage.py runserver

**Scrapper API**
1. API: /api/scrapper
2. Parameters:
   a. product:
        i. Datatype: String
        ii. Mandatory
   b. page:
        i. Datatype: Integer
        ii. Default Value: 1
        iii. Optional
3. Average Time Taken Per API call: 120 - 150 seconds.

**NOTE:** 
This server uses Amazon India website to do webscraping. Amazon blocks the hosts which try to do webscraping. To 
avoid getting blocked, this server uses 4 different user agents randomly. Incase the server gets blocked for all 4 user 
agents, then change the value of WEBSITE_URL variable in settings.py to AMAZON_US_URL to point it to Amazon USA website.
If this too gets blocked, then the user will have to add new user agents (although this is unlikely to happen easily).
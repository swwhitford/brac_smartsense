# brac
Freezer graphing scripts

Smartsense is a freezer monitoring service in use at the BRAC. Sensors on each freezer monitor temperature, which is available to the website for viewing and download. I created a scraping program in python to download monthly charts to an excel file. The excel files include a chart, and any out-of range temperatures are flagged. This allows me to download a wide timeframe, and save monthly temperature records for each freezer.

username and password for Smartsense's site (https://app.smartsense.co) should be save in a file called login.py, which contains the following text (replace xxx with your own username/password:
data = '{"userName": "xxx", "password": "xxx"}'


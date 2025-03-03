
# Rightmove Data Scraper

This script based on property data scrap from https://www.rightmove.co.uk/


## What you will get:

- All data in in a CSV file. 
- Data points are- Property URL, Name, Address, Price, Property type, Property size, Bathroom, Bedroom, Short Description, Long Description, Marketed by, Images, Attachments


## Requirement

Python, pandas, requests, Bs4, lxml


## Documentation

- Install python on your OS. You can install latest version of python.
- Now open your cmd/terminal and run those commands one by one:
```bash
  pip install pandas
  pip install bs4
  pip install lxml
  pip install requests
```
- Now we can run the script using this command from that folder terminal/cmd:
```bash
python rightmove.py
```
- After run it will ask to input a URL. You need to search your listing property page and after that go to second page. Copy that URL and put on there(cmd/terminal) and hit enter.
Ex: https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&index=24&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=
- It will automaticaly go through all pages and property pages. Save the data in a CSV file.


## Authors

- [@amitchakraborty123](https://www.github.com/amitchakraborty123)


## 🚀 About Me
I'm a Data Analyst.


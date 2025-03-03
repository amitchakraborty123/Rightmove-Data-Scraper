Rightmove Data Scraper

What you will get:
Data in a CSV file- Property URL, Name, Address, Price, Property type, Property size, Bathroom, Bedroom, Short Description, Long Description, Marketed by, Images, Attachments

Requirement: Python, pandas, requests, Bs4, lxml

Instruction to setup:
1. Install python on your OS. You can install latest version of python.
2. Now open your cmd/terminal and run those commands one by one:
pip install pandas
pip install bs4
pip install lxml
pip install requests
3. Now we can run the script using this command from that folder terminal/cmd:
python rightmove.py
4. After run it will ask to input a URL. You need to search your listing property page and after that go to second page. Copy that URL and put on there(cmd/terminal) and hit enter.
Ex: https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&index=24&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=
Process: At
5. It will automaticaly go through all pages and property pages. Save the data in a CSV file.
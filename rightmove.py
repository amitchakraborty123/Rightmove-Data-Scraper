'''
Author: Amit Chakraborty
Project: Rightmove Data Scraper
Profile URL: https://github.com/amitchakraborty123
E-mail: mr.amitc55@gmail.com
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    # 'Host' : 'https://www.zim.com/',
    'Connection': 'keep-alive',
    'User-Agent': 'Chrome/102.0.5005.63 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Safari/536.5',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'text',
    'Accept-Language': 'en-US,en;q=0.8'
}
# ================================================================================
#                         Getting Links
# ================================================================================
def get_url():
    print("====================================  Scraping Links ==================================")
    all_link = []
    input_url = input("Enter the URL: ")
    start_index = int(input_url.split('index=')[1].split('&')[0])
    page = 0
    index = 0
    limit = 0
    while True:
        page += 1
        print(f'>>>>>>>>>>>> Getting link {page}')
        main_url = input_url.replace(f'index={start_index}', f'index={index}')
        soup = BeautifulSoup(requests.get(main_url, headers=headers).content, 'lxml')
        index += 24
        if limit > 75:
            break
        try:
            divs = soup.find('div', {'id': 'l-searchResults'}).find_all('div', {'class': 'l-searchResult'})
        except:
            divs = []
        print(f'Listing here: {len(divs)}')
        if len(divs) < 1:
            break
        for div in divs:
            url = ''
            short_des = ''
            marketed_by = ''
            try:
                url = div.find('a', {'class': 'propertyCard-link'})['href']
            except:
                pass
            try:
                short_des = div.find('h2', {'class': 'propertyCard-title'}).text.replace('\n', '').strip()
            except:
                pass
            try:
                marketed_by = div.find('span', {'class': 'propertyCard-branchSummary-branchName'}).text.replace('\n', '').replace('Marketed by ', '').strip()
            except:
                pass
            link = {
                'URL': "https://www.rightmove.co.uk" + url,
                'short_des': short_des,
                'marketed_by': marketed_by,
            }
            # print(link)
            if link not in all_link:
                all_link.append(link)
            else:
                limit += 1
        df = pd.DataFrame(all_link)
        df = df.rename_axis("Index")
        df.to_csv('links.csv', encoding='utf-8-sig')



# ================================================================================
#                         Getting data
# ================================================================================
def get_data():
    print("====================================  Scraping Entire Data ==================================")
    all_data = []
    df = pd.read_csv("links.csv")
    url = df['URL'].values
    short_d = df['short_des'].values
    marketed_b = df['marketed_by'].values
    print('Total Links: ' + str(len(url)))
    ll = 0
    for i in range(0, len(df)):
        ll += 1
        link = url[i]
        short_des = short_d[i]
        marketed_by = marketed_b[i]
        print('Getting link ' + str(ll) + ' out of ' + str(len(url)))
        soup = BeautifulSoup(requests.get(link, headers=headers).content, 'lxml')
        name = ''
        all_images = ''
        address = ''
        price = ''
        property_type = ''
        property_size = ''
        bathroom = ''
        bedroom = ''
        long_des = ''
        attachments = ''
        try:
            all_images = []
            for img in soup.find_all('article')[0].find_all('meta'):
                all_images.append(img.get('content'))
            all_images = list(set(all_images))
        except:
            pass
        try:
            address = soup.find('h1', {'itemprop': 'streetAddress'}).text.replace('\n', '').split(',', 1)[-1]
        except:
            pass
        try:
            name = soup.find('h1', {'itemprop': 'streetAddress'}).text.replace('\n', '').replace(address, '').replace(',', '')
        except:
            pass
        try:
            price = soup.find_all('article')[1].find('span').text.replace('\n', '')
        except:
            pass
        try:
            temp1 = soup.find('dl', {'id': 'info-reel'}).find_all('div', {'class': '_3gIoc-NFXILAOZEaEjJi1n'})
            for dess in temp1:
                if 'PROPERTY TYPE' in dess.text:
                    property_type = dess.text.replace('PROPERTY TYPE', '').replace('\n', '')
                if 'BEDROOMS' in dess.text:
                    bedroom = dess.text.replace('BEDROOMS', '').replace('\n', '')
                if 'BATHROOMS' in dess.text:
                    bathroom = dess.text.replace('BATHROOMS', '').replace('\n', '')
                if 'SIZE' in dess.text:
                    property_size = dess.text.replace('SIZE', '').replace('\n', '')
        except:
            pass
        try:
            temp2 = soup.find_all('article')[3].find_all('div')
            for dess in temp2:
                if 'Property description' in dess.text:
                    long_des = dess.text.replace('Property description', '').replace('\n', '')
        except:
            pass
        try:
            temp5 = soup.find_all('article')[3].find_all('a')
            for attr in temp5:
                if ".pdf" in attr.get("href"):
                    temp3 = (attr.get("href"), attr.text)
            temp6 = link.split('#')[0]
            for attr in temp5:
                if "/floorplan" in attr.get("href"):
                    temp4 = (str(temp6) + attr.get("href"), attr.text)
            attachments = temp3 + temp4
        except:
            pass
        data = {
            'URL': link,
            'Name': name,
            'Address': address,
            'Price': price,
            'Property type': property_type,
            'Property size': property_size,
            'Bathroom': bathroom,
            'Bedroom': bedroom,
            'Short Description': short_des,
            'Long Description': long_des,
            'Marketed by': marketed_by,
            'Images': ", ".join(all_images),
            'Attachments': ", ".join(attachments).replace('Brochure 1', ''),
        }
        # print(data)
        all_data.append(data)
        df = pd.DataFrame(all_data)
        df = df.rename_axis("Index")
        df.to_csv('Final_data.csv', encoding='utf-8-sig')
    df = pd.DataFrame(all_data)
    df = df.rename_axis("Index")
    df.to_csv('Final_data.csv', encoding='utf-8-sig')


if __name__ == '__main__':
    # get_url()
    get_data()
from bs4 import BeautifulSoup
import requests
import csv


def get_freelancer_info(freelancers):
    freelancer_information = []
    for freelancer in freelancers:
        freelancer_dict = {}
        endpoint = url  + freelancer
        r = requests.get(endpoint)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        
        name = soup.find('h2', class_="profile-intro-username").text.strip()
        location = soup.find('span', attrs={'itemprop': 'addressLocality'}).text
        rating = soup.find('meta', attrs={'itemprop': 'ratingValue'}, content=True)['content']
        

        freelancer_dict['location'] = location
        freelancer_dict['rating'] = rating
        freelancer_dict['name'] = name


        freelancer_information.append(freelancer_dict)

    return freelancer_information


def writeToCSV(freelancer_data):

    print(freelancer_data[0])

    keys = freelancer_data[0].keys()

    with open('freelancers.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(freelancer_data)





url = 'https://freelancer.com'

skills['Javascript', 'PHP', 'Java', 'Copywriting', 'Technical Writing', 'Ghostwriting', 'MySQL',
        'CSS', 'Web Scraping', 'Data Mining', 'Accounting', 'Advertising']
    

search_freelancers = 'https://www.freelancer.com/freelancers/United_States/Website_Design/2'

r = requests.get(search_freelancers)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

freelancers = []
for a in soup.find_all('a',attrs={'hireme-event': 'ProfileRedirect'}, href=True):
    freelancers.append(a['href'])

freelancers = list(set(freelancers))

freelancer_info = get_freelancer_info(freelancers)

writeToCSV(freelancer_info)

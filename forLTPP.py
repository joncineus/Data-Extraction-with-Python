import requests 
from bs4 import BeautifulSoup
import regex as re

section_IDs = input("Please input the states you want selected: ")
section_ID_list = re.split(', ', section_IDs)

for section in section_ID_list:
    html_text = requests.get(f"https://infopave.fhwa.dot.gov/Data/PrintReport/?Section={section}&Type=Single&unit=df&SectionId=1806").text

    soup = BeautifulSoup(html_text, 'lxml')

    first = soup.find('div', id="SectionSummaryReport")
    #Gets the entire selection of tables

    second = first.find('div', id="DataMainDiv")

    third = second.find('table', class_="container")

    fourth = third.find_all('tbody')[2]

    fifth = fourth.find_all('tr')

 
    list = fifth[1].find_all('td', class_='tdLeft center cell1')
    date = list[2].text
    event= list[3].text
    print(date)

    for item in fifth:
        list = item.find_all('td', class_='tdLeft center cell1')
        date = list[2].text
        event= list[7].text
        print(event)



import requests 
from bs4 import BeautifulSoup
import regex as re

inputted_date= ""
program_date = ""
search_date = 0

list_dates = []

date_count = 0

section_IDs = input("Please input the sections you want selected: ")
section_ID_list = re.split(',', section_IDs)

for section in section_ID_list:
    html_text = requests.get(f"https://infopave.fhwa.dot.gov/Data/PrintReport/?Section={section}&Type=Single&unit=df&SectionId=1806").text

    soup = BeautifulSoup(html_text, 'lxml')

    first = soup.find('div', id="SectionSummaryReport")
    #Gets the entire selection of tables

    second = first.find('div', id="DataMainDiv")

    third = second.find('table', class_="container")

    fourth = third.find('tr', align="left")

    fifth = fourth.find('td', id="latlong").text

    lat = re.split(",", fifth)[0]

    lat = float(lat)

    if lat <= 36.7378:
        print(section)

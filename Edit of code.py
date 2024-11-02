import requests 
from bs4 import BeautifulSoup
import regex as re
from datetime import date

section_IDs = input("Please input the sections you want selected: ")
section_ID_list = re.split(', ', section_IDs)

skid_date = input("Please input the dates for the full sections: ")
skid_date_list = re.split(', ', skid_date)

for section in section_ID_list:
    html_text = requests.get(f"https://infopave.fhwa.dot.gov/Data/PrintReport/?Section={section}&Type=Single&unit=df&SectionId=1806").text

    soup = BeautifulSoup(html_text, 'lxml')

    first = soup.find('div', id="SectionSummaryReport")
    #Gets the entire selection of tables

    second = first.find('div', id="DataMainDiv")

    third = second.find('table', class_="container")

    fourth = third.find_all('tbody')[2]

    fifth = fourth.find_all('tr')

    date_comp_list = []
    date_objects = []


    #Puts the list of dates from the webpage into a list
    for item in fifth:
        list = item.find_all('td', class_='tdLeft center cell1')
        date = list[2].text

        #This validates whether the test is a date
        if "-" in date:
            #This specifically gets part of the date that we need without spaces
            date_comp_list.append(date[0:10]) 
        

    #Converting the availiable dates into numbers
    #First split the values into date objects
    for i in date_comp_list:
        date_split = re.split("-", i)
    

        
    




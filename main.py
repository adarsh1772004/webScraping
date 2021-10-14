from bs4.element import TemplateString
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome(
    "C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(start_url)
time.sleep(10)


def scrap():
    headers = ["NAME", "LIGHT_YEARS_FROM_EARTH",
               "PLANET_MASS", "STELLAR_MAGNITUDE", "DISCOVERY_DATE"]
    planet_data = []
    for i in range(0, 10):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append(
                            "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/")

            planet_data.append(temp_list)
            browser.find_element_by_xpath(
                '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("scrapper.csv", "w") as f:
        csvwritter = csv.writer(f)
        csvwritter.writerow(headers)
        csvwritter.writerows(planet_data)


scrap()

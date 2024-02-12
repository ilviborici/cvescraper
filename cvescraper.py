import requests
from bs4 import BeautifulSoup

page = 1
kev_pages = []
while page < 6:
    URL = f"https://www.cisa.gov/known-exploited-vulnerabilities-catalog?page={page}"
    response = requests.get(URL)
    page = page + 1
    soup = BeautifulSoup(response.content, "html.parser")
    job_elements = soup.find_all("div", class_="c-view__row")

    with open('cve_results.txt', 'a') as f:
        for job_element in job_elements:
            number_element = job_element.find("h3", class_="c-teaser__title")
            name_element = job_element.find("div", class_='c-teaser__vuln-name')
            summary_element = job_element.find("div", class_="c-teaser__summary")

            f.write("Number: " + number_element.text.strip() + "\n")
            f.write("Title: " + name_element.text.strip() + "\n")
            f.write("Summary: " + summary_element.text.strip() + "\n\n")

            kev_pages.append(number_element.text.strip())

        f.write("Total CVEs: " + str(len(kev_pages)) + "\n")

from bs4 import BeautifulSoup

from src.logger import #LOGGER
from src.utils import write_json_file

from bs4 import BeautifulSoup


def extract_language_names():
    # Read the HTML file
    with open('src/input/language_list.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all unordered lists (ul) and then find all list items (li) within them
    all_lists = soup.find_all('ul')

    language_list = []

    for ul in all_lists:
        list_items = ul.find_all('li')

        for item in list_items:
            link_tag = item.find('a')
            if link_tag:
                link = link_tag.get('href')
                title = link_tag.get('title')
                language_list.append({'link': 'https://esolangs.org' + link, 'title': title})

    #LOGGER.info(f"Extracted {len(language_list)} language names")

    write_json_file('src/output/languages.json', language_list)


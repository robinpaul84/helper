import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "https://apod.nasa.gov/apod/archivepix.html"
output_folder = "images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

link_to_visit = set((base_url,))
link_visited = set()

while link_to_visit:
    current_page = link_to_visit.pop()
    print("Visiting:", current_page)
    link_visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()

    # Extract new links from the visited page
    for link in BeautifulSoup(content,"lxml").findAll("a"):
        absolute_link = urljoin(current_page,link["href"])
        if absolute_link not in link_visited:
            link_to_visit.add(absolute_link)
        else:
            print("Already Visited: ", absolute_link)

    # Download all images on the page
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(output_folder, img_name))
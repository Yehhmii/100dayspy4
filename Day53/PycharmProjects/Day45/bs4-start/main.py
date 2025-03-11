from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")
article_list = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for articles in article_list:
    article_tag = articles.find(name="a")

    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_points)
largest_index = article_points.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_points)















#
# with open("website.html", encoding="utf8") as file:
#     website_data = file.read()
#
# soup = BeautifulSoup(website_data, "lxml")
# # print(soup)
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# tags = soup.find_all(name="a")
# # print(tags)
# # for tag in tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.name)
# # print(section_heading.getText)
# # print(section_heading.string)
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)

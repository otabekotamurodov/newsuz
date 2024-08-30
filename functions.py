import requests
from bs4 import BeautifulSoup


def daryo_articles():
    URL = "https://daryo.uz/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="media")
    articles_for_web = []
    for i in range(len(articles)):
        a_tag = articles[i].find("a")
        if a_tag:
            title = a_tag.get("title")
            url = URL + a_tag.get("href")
            span_tag = a_tag.find("span")
            if span_tag and span_tag.get("data-bgsrc"):
                image = URL + span_tag.get("data-bgsrc")
            else:
                # Fallback to <img> tag if <span> is not found
                img_tag = a_tag.find("img")
                if img_tag and img_tag.get("src"):
                    image = URL + img_tag.get("src")
                else:
                    # Set image to None if no valid image is found
                    image = None

            articles_for_web.append({
                "title": title,
                "url": url,
                "image": image,
            })

    return articles_for_web


def daryo_article(title, link, image_link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find_all("div", class_="the-post s-post-modern")[0].find_all("article")[0].find_all("div")[0].find_all("div")[0].text
    return {"title": title,
            "image": image_link,
            "text": text}

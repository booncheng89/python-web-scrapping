from requests import get
from bs4 import BeautifulSoup


if __name__ == '__main__':
    resp = get(url="https://www.byprogrammers.com/blog/")

    # if status code = 200 then proceed else print error
    if resp.status_code == 200:
        html_doc = resp.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        posts = soup.find_all("div", "post-inner-content")


        for post in posts:
            title = post.header.h2.text
            author = post.find("span", "author vcard").text
            print("Title: {}".format(title))
            print("Author: {}".format(author))

    else:
        print("Fail to load web page")

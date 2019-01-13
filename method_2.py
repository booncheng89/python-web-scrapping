from selenium import webdriver

def start_browser():
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver

if __name__ == '__main__':
    br = start_browser()
    br.get(url="https://www.byprogrammers.com/blog/")
    # wait 5s to load web page
    br.implicitly_wait(5)

    posts = br.find_elements_by_class_name("post-inner-content")

    for post in posts:
        title = post.find_element_by_tag_name("h2").text
        author = post.find_element_by_class_name("author").text
        print("Title: {}".format(title))
        print("Author: {}".format(author))


    br.close()

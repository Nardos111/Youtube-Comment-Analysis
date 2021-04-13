import time
import csv
import io
from selenium import webdriver
from selenium.common import exceptions


def scrape(url):
    driver = webdriver.Chrome("./webdrivers/chromedriver")
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    try:
        # Extract the elements storing the video title and comment section
        title = driver.find_element_by_xpath(
            '//*[@id="container"]/h1/yt-formatted-string').text
        comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
    # Raise an error in case elements provided cannot be found
    except exceptions.NoSuchElementException:
        error = "Can't find element"
        print(error)

    # Scroll into view the comment section, allow some time for everything to load
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(7)

    # Scroll all the way down to the bottom in order to get all the elements loaded
    last_height = driver.execute_script(
        "return document.documentElement.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # One last scroll
    driver.execute_script(
        "window.scrollTo(0, document.documentElement.scrollHeight);")

    try:
        # Extract elements storing username and comment
        username_elems = driver.find_elements_by_xpath(
            '//*[@id="author-text"]')
        comment_elems = driver.find_elements_by_xpath(
            '//*[@id="content-text"]')

    except exceptions.NoSuchElementException:
        error = "Can't find element"
        print(error)

    print("> VIDEO TITLE: " + title + "\n")

    with io.open('results.csv', 'w', newline='', encoding="utf-16") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["Username", "Comment"])
        for username, comment in zip(username_elems, comment_elems):
            writer.writerow([username.text, comment.text])

    driver.close()


if __name__ == "__main__":
    scrape("https://www.youtube.com/watch?v=26vwOR1oCGE&ab_channel=LekemAmsal")

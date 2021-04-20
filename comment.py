import time
import csv
import io
from selenium import webdriver
from selenium.common import exceptions
from emotion_detection import posaneg


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
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight")
        read_more = driver.find_element_by_xpath(
            '//*[@id="more"]/yt-formatted-string')
        driver.execute_script("arguments[0].click();", read_more)
        sort_by = driver.find_element_by_xpath(
            '//*[@id="label" and @class="dropdown-trigger style-scope yt-dropdown-menu"]')
        driver.execute_script("arguments[0].click();", sort_by)
        topComment = driver.find_element_by_xpath(
            '//*[@id="menu"]/a[1]/tp-yt-paper-item')
        driver.execute_script("arguments[0].click();", topComment)

        if new_height == last_height:
            break
        last_height = new_height

    # One last scroll
    driver.execute_script(
        "window.scrollTo(0, document.documentElement.scrollHeight);")

    try:

        username_elems = driver.find_elements_by_xpath(
            '//*[@id="author-text"]')

        # driver.find_element_by_id('//*[@id="more"]').click()
        comment_elems = driver.find_elements_by_xpath(
            '//*[@id="content-text"]')
    except exceptions.NoSuchElementException:
        error = "Can't find element"
        print(error)
    with io.open('results.csv', 'w', newline='', encoding="utf-16") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(["Username", "Comment"])
        for username, comment in zip(username_elems, comment_elems):
            writer.writerow([username.text, comment.text])

    duration = driver.find_element_by_class_name("ytp-time-duration").text
    views = driver.find_element_by_xpath(
        '//*[@id="count"]/ytd-video-view-count-renderer/span').text
    likes = driver.find_element_by_xpath(
        '(//yt-formatted-string[@id="text" and @class="style-scope ytd-toggle-button-renderer style-text"])[1]').get_attribute("aria-label")
    dislikes = driver.find_element_by_xpath(
        '(//yt-formatted-string[@id="text" and @class="style-scope ytd-toggle-button-renderer style-text"])[2]').get_attribute("aria-label")
    more = driver.find_element_by_xpath('//*[@id="more"]/yt-formatted-string')
    driver.execute_script("arguments[0].click();", more)

    descriptions = driver.find_elements_by_xpath(
        '//*[@id="description"]/yt-formatted-string')
    texts = []
    for description in descriptions:
        text = description.text
        texts.append(text)

    desc = texts[0].replace("\n", "")
    info = [duration, views, likes, dislikes, desc, title]

    with io.open('video_info.csv', 'w', newline='', encoding="utf-16") as file:
        writer = csv.writer(file)
        writer.writerow([info])

    driver.quit()
    time.sleep(5)
    posaneg()
    return ('', 204)

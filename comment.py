from selenium import webdriver
import time
import os
import csv
import pandas as pd
from math import ceil
from selenium.common.exceptions import NoSuchElementException
from urllib import request


def scrape(url):
    csv_file = open('./output_scraping.csv', 'w', encoding="UTF-8", newline="")
    csv_file2 = open('./video_info.csv', 'w', encoding="UTF-8", newline="")
    writer = csv.writer(csv_file)
    writer2 = csv.writer(csv_file2)
    writer.writerow(
        ['number', 'comment', 'upvotes'])
    writer2.writerow(['url', 'link_title', 'description', 'channel',
                      'no_of_views', 'time_uploaded', 'likes', 'dislikes'])
    youtube_pages = "https://www.youtube.com/"
    locationOfWebdriver = "./webdrivers/chromedriver"
    driver = webdriver.Chrome(locationOfWebdriver)
    driver.get(youtube_pages)
    time.sleep(10)
    try:
        print("=" * 40)
        print("Scraping " + youtube_pages)
        search = driver.find_element_by_id('search')
        search.send_keys(url)
        driver.find_element_by_id('search-icon-legacy').click()
        time.sleep(20)
        vtitle = driver.find_elements_by_xpath(
            '//a[@id="video-title" and @class="yt-simple-endpoint style-scope ytd-video-renderer"]')
        images = driver.find_elements_by_xpath(
            '//div[@id="dismissible" and @class="style-scope ytd-video-renderer"]//a[@id="thumbnail" and @class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]//img[@id="img" and @class="style-scope yt-img-shadow"]')
        tcount = 0
        href = []
        title = []
        image_urls = []
        while tcount < 2:
            href.append(vtitle[tcount].get_attribute('href'))
            title.append(vtitle[tcount].text)
            image_urls.append(images[tcount].get_attribute('src'))
            tcount += 1
        tcount = 0
        print(image_urls)
        while tcount < 2:
            youtube_dict = {}
            url = href[tcount]

            request.urlretrieve(
                image_urls[tcount], "./static/%s.jpg" % str(tcount+1))

            driver.get(url)
            time.sleep(5)
            try:
                print("+" * 40)
                print("Scraping child links ")
                numview = driver.find_element_by_xpath(
                    '//*[@id="count"]/ytd-video-view-count-renderer/span').text
                uploaddate = driver.find_element_by_xpath(
                    '//div[@id="info-strings" and @class="style-scope ytd-video-primary-info-renderer"]//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]').text
                likes = driver.find_element_by_xpath(
                    '(//yt-formatted-string[@id="text" and @class="style-scope ytd-toggle-button-renderer style-text"])[1]').get_attribute("aria-label")
                dislikes = driver.find_element_by_xpath(
                    '(//yt-formatted-string[@id="text" and @class="style-scope ytd-toggle-button-renderer style-text"])[2]').get_attribute("aria-label")
                channel = driver.find_element_by_xpath(
                    '//div[@id="text-container" and @class="style-scope ytd-channel-name"]//yt-formatted-string[@id="text" and @class="style-scope ytd-channel-name"]//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]').text
                driver.execute_script('window.scrollTo(0,390);')
                time.sleep(20)
                try:
                    sort = driver.find_element_by_xpath(
                        """//*[@id="icon-label"]""")
                    sort.click()
                    time.sleep(10)
                    topComment = driver.find_element_by_xpath(
                        '//*[@id="menu"]/a[1]/tp-yt-paper-item')
                    driver.execute_script("arguments[0].click();", topComment)
                except NoSuchElementException:
                    sort = ""
                try:
                    more = driver.find_element_by_xpath(
                        '//*[@id="more"]/yt-formatted-string')
                    driver.execute_script("arguments[0].click();", more)
                except NoSuchElementException:
                    more = ""
                descriptions = driver.find_elements_by_xpath(
                    '//*[@id="description"]/yt-formatted-string')
                texts = []
                for description in descriptions:
                    text = description.text
                    texts.append(text)
                desc = texts[0].replace("\n", "")
                description_dict = {}
                description_dict['url'] = href[tcount]
                description_dict['link_title'] = title[tcount]
                description_dict['description'] = desc
                description_dict['channel'] = channel
                description_dict['no_of_views'] = numview
                description_dict['time_uploaded'] = uploaddate
                description_dict['likes'] = likes
                description_dict['dislikes'] = dislikes
                writer2.writerow(description_dict.values())
                time.sleep(10)
                # Loads 20 comments , scroll two times to load next set of 40 comments.
                for i in range(0, 2):
                    driver.execute_script(
                        "window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight))")
                    time.sleep(10)

                # count total number of comments and set index to number of comments if less than 50 otherwise set as 50.
                totalcomments = len(driver.find_elements_by_xpath(
                    """//*[@id="content-text"]"""))

                if totalcomments < 50:
                    index = totalcomments
                else:
                    index = 50

                ccount = 0
                while ccount < index:
                    try:
                        comment = driver.find_elements_by_xpath(
                            '//*[@id="content-text"]')[ccount].text
                    except:
                        comment = ""
                    try:
                        upvotes = driver.find_elements_by_xpath(
                            '//*[@id="vote-count-middle"]')[ccount].text
                    except:
                        upvotes = ""

                    youtube_dict['number'] = tcount
                    youtube_dict['comment'] = comment
                    youtube_dict['upvotes'] = upvotes

                    writer.writerow(youtube_dict.values())
                    ccount = ccount + 1

            except Exception as e:
                print(e)
                driver.close()
            tcount = tcount + 1
        print("Scrapping process Completed")
        csv_file.close()
        csv_file2.close()
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
    return ('', 204)

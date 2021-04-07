import time
import selenium
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# scroll down
# wait for comments to appear
# scrape the comments
# repeat for some range

data = []
with Chrome(executable_path=r'./chromedriver') as driver:
    wait = WebDriverWait(driver, 15)
    driver.get(
        "https://www.youtube.com/watch?v=26vwOR1oCGE&ab_channel=LekemAmsal")
    for item in range(10):
        wait.until(EC.visibility_of_element_located(
            (By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment"))):
        data.append(comment.text)


# df = pd.DataFrame(data, columns=['comment'])
# df.head()

for item in data:
    print(item)

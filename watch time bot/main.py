import time
from selenium import webdriver

video_link = 'https://youtu.be/UjDYNWkwZAo'
views = 100
video_duration = 7 * 60

driver = webdriver.Chrome()
driver.get(video_link)

for i in range(views):
    time.sleep(video_duration)
    driver.refresh()

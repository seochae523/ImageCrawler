import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import ssl
import os

address = '/Users/chaeyun/Documents/img'
URL = "https://ide.mblock.cc/"
driver = webdriver.Chrome("/Users/chaeyun/PycharmProjects/crawler/chromedriver")

def init():
    ssl._create_default_https_context = ssl._create_unverified_context


def openSpriteWeb():
    driver.get(URL)  # 크롬 창 오픈
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@id="pageLoading"]')))  # 로딩 페이지 사라질때까지 기다리기
    time.sleep(0.5)  # 추가 대기
    driver.find_element_by_xpath(
        '//*[@id="mblockApp"]/section/section[1]/aside/div/section/main/section/header/div/div[2]').click()  # 스프라이트 버튼 클릭
    driver.find_element_by_xpath(
        '//*[@id="mblockApp"]/section/section[1]/aside/div/section/main/section/main/section/aside/div/section/div[4]/div/div/div/div[2]/div/div[1]/button').click()  # 모양 버튼 클릭
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="mblockApp"]/section/section[1]/main/section/section[1]/div[2]/div/div/div/div/div/section/aside/div/section/footer/button')))  # 모양 추가 버튼 나오는 모션 기다리기
    time.sleep(0.5)  # 추가 대기
    driver.find_element_by_xpath(
        '//*[@id="mblockApp"]/section/section[1]/main/section/section[1]/div[2]/div/div/div/div/div/section/aside/div/section/footer/button').click()  # 모양 추가 버튼 클릭


def crwalByCatagories():
    time.sleep(5)
    for idx in range(2, 14):
        categorie = driver.find_element_by_xpath(
            '// *[ @ id = "rc-tabs-0-panel-sprite"] / section / header / section / button[' + str(idx) + ']')
        categorieName = categorie.get_attribute('data-tag')
        categorie.click()
        outPath = '/Users/chaeyun/Documents/sprite/' + categorieName + '/'
        if not os.path.isdir(outPath):  # 폴더가 존재하지 않는다면 폴더 생성
            os.makedirs(outPath)

        for i in range(1, 21):
            for itemIdx in range(1, 43):
                try:
                    itemUrl = driver.find_element_by_xpath(
                        '// *[ @ id = "rc-tabs-0-panel-sprite"] / section / main / section / div[4] / div / div / div / div[1] / div / div / div[' + str(
                            itemIdx) + '] / div / div / div / picture / img')
                    itemUrl = itemUrl.get_attribute('src')
                    itemName = driver.find_element_by_xpath(
                        '// *[ @ id = "rc-tabs-0-panel-sprite"] / section / main / section / div[4] / div / div / div / div[1] / div / div / div[' + str(
                            itemIdx) + '] / div / div / div / div / p / span')
                    itemName = itemName.get_attribute('title')

                    urllib.request.urlretrieve(itemUrl,
                                               '/Users/chaeyun/Documents/sprite/' + categorieName + '/' + itemName + '.svg')
                except:
                    break
            try:
                driver.find_element_by_css_selector(
                    '#rc-tabs-0-panel-sprite > section > main > section > div.os-padding > div > div > div > div.ant-list-pagination > ul > li.ant-pagination-item.ant-pagination-item-' + str(
                        i)).click()  # 다음으로 가는 버튼 클릭
            except:
                break


init()
openSpriteWeb()
crwalByCatagories()
driver.close()

import random

from selenium.webdriver.common.by import By


class Locators:
    title = random.randint(1, 40)
    SEARCH_STRING = (By.XPATH,
                     '//*[@id="app"]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input')
    FIND_BUTTON = (By.CSS_SELECTOR, 'button[class="desktop-15w37ob"]')
    TITLE = (By.XPATH,
             f'//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[{title}]')
    FAVORITES_ADD = (By.XPATH, f'//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div[2]/'
                               f'div[{title}]/div/div/div[2]/div[1]')
    NAME = (By.XPATH, f'//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div[2]/'
                      f'div[{title}]/div/div/div[2]/div[2]/div/a/h3')
    FAVORITES_MENU = (By.CSS_SELECTOR, 'div[class="desktop-1rdftp2"]')
    FAVORITE_TITLE = (By.CSS_SELECTOR, 'strong[class="styles-module-root-hwVld"]')
    NAME_FROM_TITLE = (By.CSS_SELECTOR, 'span[class="title-info-title-text"]')
    BUTTON_FAVORITE = (By.CSS_SELECTOR, 'div[class="style-header-add-favorite-M7nA2"]>button')
    FAVORITE_DEL = (By.CSS_SELECTOR, 'div[class="withFavorites-heart-x57Yw withFavorites-heart_fill-InZcS"]')
    FAVORITE_TEXT = (By.CSS_SELECTOR, 'h3[class*="styles-module-root-uSima styles-module-root-xvjz8"]')
    MAIN_PAGE = (By.CSS_SELECTOR, 'div[class="index-logo-ykryA"]')
    MAIN_PAGE_FROM_FAVORITE = (By.CSS_SELECTOR, 'div[class="index-logo-K90gi"]')
    TITLE_FROM_FAVORITE_MENU = (By.CSS_SELECTOR, 'a[class="css-1e7cqb"]')

from selenium.webdriver.common.by import By


class Locators:
    SEARCH_STRING = (By.XPATH,
                     '//*[@id="app"]/div/div[3]/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div/label[1]/input')
    FIND_BUTTON = (By.CSS_SELECTOR, 'button[class="desktop-8ydzks"]')
    ITEM = (By.CSS_SELECTOR, 'div[class="items-items-kAJAg"]')
    TITLE = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[5]')
    FAVORITES_ADD = (By.CSS_SELECTOR, 'div[class="iva-item-favoritesStep-__W3E"]')
    NAME = (By.XPATH, '//div[@class="iva-item-title-py3i_"]//h3')
    FAVORITES_MENU = (By.CSS_SELECTOR, 'div[class="desktop-1rdftp2"]')
    FAVORITE_NAME = (By.CSS_SELECTOR, 'a[class="css-1e7cqb"]')
    FAVORITE_TITLE = (By.CSS_SELECTOR, 'strong[class="styles-module-root-hwVld"]')
    NAME_FROM_TITLE = (By.CSS_SELECTOR, 'span[class="title-info-title-text"]')
    BUTTON_FAVORITE = (By.CSS_SELECTOR, 'div[class="style-header-add-favorite-M7nA2"]')
    FAVORITE_DEL = (By.CSS_SELECTOR, 'div[class="withFavorites-heart-x57Yw withFavorites-heart_fill-InZcS"]')
    FAVORITE_TEXT = (By.CSS_SELECTOR, 'h3[class*="styles-module-root-uSima styles-module-root-xvjz8"]')
    MAIN_PAGE = (By.CSS_SELECTOR, 'div[class="index-logo-ykryA"]')

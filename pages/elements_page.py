from locators.form_page_locators import Locators
from pages.base_page import BasePage


class TextPages(BasePage):
    locators = Locators()

    def add_domain_driver(self):
        expected_result = []
        result = []

        self.element_is_clickable(self.locators.BUTTON_FAVORITE).click()
        expected_result.append(self.element_is_visible(self.locators.NAME_FROM_TITLE).text)
        self.element_is_clickable(self.locators.FAVORITES_MENU).click()
        result.append(self.element_is_visible(self.locators.FAVORITE_TITLE).text)

        return expected_result, result

    def add_from_search(self):
        search = ['самокаты', 'телефоны', 'одежда']

        expected_result = []
        result = []

        for item in search:
            self.element_is_visible(self.locators.SEARCH_STRING).send_keys(item)
            self.element_is_clickable(self.locators.FIND_BUTTON).click()
            self.element_is_clickable(self.locators.FAVORITES_ADD).click()
            expected_result.append(self.elements_are_visible(self.locators.NAME)[0].text)
            self.element_is_clickable(self.locators.FAVORITES_MENU).click()
            result.append(self.element_is_present(self.locators.FAVORITE_TITLE).text)
            self.element_is_clickable(self.locators.FAVORITE_DEL).click()
            self.element_is_clickable(self.locators.MAIN_PAGE).click()

        return expected_result, result

    @property
    def add_from_title(self):
        search = ['самокаты', 'телефоны', 'одежда']

        expected_result = []
        result = []

        main_window = self.driver.current_window_handle

        for item in search:

            self.element_is_visible(self.locators.SEARCH_STRING).send_keys(item)
            self.element_is_clickable(self.locators.FIND_BUTTON).click()
            self.element_is_clickable(self.locators.TITLE).click()
            all_windows = self.driver.window_handles

            for window in all_windows:
                if window != main_window:
                    self.driver.switch_to.window(window)
                    self.element_is_clickable(self.locators.BUTTON_FAVORITE).click()
                    expected_result.append(self.element_is_visible(self.locators.NAME_FROM_TITLE).text)
                    self.driver.close()
                    self.driver.switch_to.window(main_window)

            self.element_is_clickable(self.locators.FAVORITES_MENU).click()
            result.append(self.element_is_visible(self.locators.FAVORITE_TITLE).text)
            self.element_is_clickable(self.locators.FAVORITE_DEL).click()
            self.element_is_clickable(self.locators.MAIN_PAGE).click()

        return expected_result, result

    @property
    def del_from_title(self):
        search = ['самокаты', 'телефоны', 'одежда']

        expected_result = 'Сохраняйте объявления'
        result = []

        main_window = self.driver.current_window_handle

        for item in search:
            self.element_is_visible(self.locators.SEARCH_STRING).send_keys(item)
            self.element_is_clickable(self.locators.FIND_BUTTON).click()
            self.element_is_clickable(self.locators.TITLE).click()
            all_windows = self.driver.window_handles

            for window in all_windows:
                if window != main_window:
                    self.driver.switch_to.window(window)
                    self.element_is_clickable(self.locators.BUTTON_FAVORITE).click()
                    self.driver.close()
                    self.driver.switch_to.window(main_window)
            self.element_is_clickable(self.locators.FAVORITES_MENU).click()
            self.element_is_clickable(self.locators.TITLE_FROM_FAVORITE_MENU).click()
            self.element_is_clickable(self.locators.BUTTON_FAVORITE).click()
            self.element_is_clickable(self.locators.MAIN_PAGE_FROM_FAVORITE).click()
        self.element_is_clickable(self.locators.FAVORITES_MENU).click()
        result.append(self.element_is_visible(self.locators.FAVORITE_TEXT).text)

        return expected_result, result

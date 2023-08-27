import pytest

from elements_page import TextPages


class TestElements:

    def test_add_domain_driver(self, driver):
        text_box_page = (
            TextPages(driver, 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain'
                              '-driven_design_distilled_vaughn_vernon_2639542363'))
        text_box_page.open()
        result, expected_result = text_box_page.add_domain_driver()
        assert result == expected_result, 'Данные не совпадают'

    def test_add_favorite_from_search(self, driver):
        text_box_page = TextPages(driver, 'https://www.avito.ru/')
        text_box_page.open()
        result, expected_result = text_box_page.add_from_search()
        assert result == expected_result, 'Данные не совпадают'

    def test_add_favorite_from_title(self, driver):
        text_box_page = TextPages(driver, 'https://www.avito.ru/')
        text_box_page.open()
        result, expected_result = text_box_page.add_from_title()
        assert result == expected_result, 'Данные не совпадают'

    def test_del_favorite_from_title(self, driver):
        text_box_page = TextPages(driver, 'https://www.avito.ru/')
        text_box_page.open()
        result, expected_result = text_box_page.del_from_title()
        assert result == expected_result, 'Данные не совпадают'

if __name__ == "__main__":
    pytest.main()


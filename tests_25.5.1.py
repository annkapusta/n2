import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('annkapusta/PycharmProjects/chromedriver')
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

def test_show_my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('ann.kapusta@mail.ru')
    # ввести пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('123123')
    # надать на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # проверить, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # неявное ожидание
    pytest.driver.implicitly_wait(10)
    # явное ожидание
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))


    images = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-title')))
    descriptions = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-text')))

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
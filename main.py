import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def switch_between_windows(windows):
    if len(windows) < 1:
        print("Windows list is empty.")
    else:
        for i in windows:
            driver.switch_to.window(driver.window_handles[i])
            time.sleep(2)


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)
base_url = "https://demoqa.com/browser-windows"
driver.get(base_url)
driver.maximize_window()

# Открываем и переключаемся на новую вкладку.
driver.find_element(By.XPATH, "//button[@id='tabButton']").click()
switch_between_windows([1,0])

# Открываем и переключаемся на новое окно.
driver.find_element(By.XPATH, "//button[@id='windowButton']").click()
switch_between_windows([2,0])

# Задержка 5 секунд и закрытие браузера
time.sleep(3)
driver.quit()
print("\nBrowser is closed")
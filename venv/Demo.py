from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(r"C:\Users\slawek\PycharmProjects\pure_selenium\drivers\chromedriver.exe")
# ...     Driver wykorzystany z uzyciem pliku w katalogu
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"C:\Users\slawek\Downloads\selenium_pliki\Test.html")
driver.maximize_window()
#driver.find_element_by_xpath('//*[@id="newPage"]').click()
#driver.quit()   # zamyka wszystkie okna, metoda .close() zamyka okno na ktorej byl focus
#driver.close()
driver.find_element(By)
driver.find_element_by_id("fname").click()
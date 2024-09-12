from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import random



chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(5)


laptops = driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2 = driver.find_element(By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]')
laptops_2.click()
time.sleep(1)


HP = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
HP.click()


add_to_button_2 = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(1)


first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)


next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

for i in range(0, 2):
    next_click.click()
    time.sleep(1)


driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')


x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)


calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar = driver.find_element(By.XPATH, '//th[@class="next"]')
month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')


while month_year.text != 'December 2023':
    next_click_calendar.click()
time.sleep(2)


calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
calendar_date.click()
time.sleep(2)


quantity = driver.find_element(By.ID, 'input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)


add_to_button = driver.find_element(By.ID, 'button-cart')
add_to_button.click()
time.sleep(2)


go_to_cart = driver.find_element(By.ID, 'cart-total')
go_to_cart.click()
time.sleep(1)

checkout = driver.find_element(By.XPATH, '//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(5)


guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
guest.click()


continue_1 = driver.find_element(By.ID, 'button-account')
continue_1.click()
time.sleep(1)


step_2 = driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)


first_name = driver.find_element(By.ID, 'input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)


last_name = driver.find_element(By.ID, 'input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)


email = driver.find_element(By.ID, 'input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)


telephone = driver.find_element(By.ID, 'input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)


address = driver.find_element(By.ID, 'input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)


city = driver.find_element(By.ID, 'input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Bucuresti')
time.sleep(1)


postcode = driver.find_element(By.ID, 'input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


country = driver.find_element(By.ID, 'input-payment-country')
dropdown_1 = Select(country)
time.sleep(1)
dropdown_1.select_by_visible_text('Romania')
time.sleep(1)


region = driver.find_element(By.ID, 'input-payment-zone')
dropdown_2 = Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Bucuresti')
time.sleep(1)


continue_2 = driver.find_element(By.XPATH, '//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)


continue_3 = driver.find_element(By.XPATH, '//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)


t_e = driver.find_element(By.XPATH, '//input[@name="agree"]')
t_e.click()
time.sleep(1)


continue_4 = driver.find_element(By.XPATH, '//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)


final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(2)


confirmation_button = driver.find_element(By.ID, 'button-confirm')
confirmation_button.click()
time.sleep(2)


success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.quit()
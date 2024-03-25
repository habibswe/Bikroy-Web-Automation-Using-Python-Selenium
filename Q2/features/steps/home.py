import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# senario number 1
@Given('launch chrome browser')
def launch_browser(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://bikroy.com/en")


@Then('verify that the logo is present on the page')
def verify_logo(context):
    Bikroy = context.browser.find_element(By.XPATH, "//a[@title='Bikroy - the largest marketplace in Bangladesh']")
    Bikroy.click()
    time.sleep(10)


# senario number 2
@when('search box write cycle')
def search_cycle(context):
    time.sleep(2)
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("cycle")


@Then('click on search')
def icon_click(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)


# senario number 3
@when('click on mobiles')
def search_mobile(context):
    mobiles = context.browser.find_element(By.XPATH, "//p[normalize-space()='Mobiles']")
    mobiles.click()
    time.sleep(10)


@Then('search mobile model')
def find_mobile(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Redmi note 8")
    time.sleep(5)


@When('click on search icon')
def click_search_icon(context):
    search = context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)


# Browse items by category(electronics)
@when('click on electronics')
def search_electronics(context):
    electronics = context.browser.find_element(By.XPATH, "//p[normalize-space()='Electronics']")
    electronics.click()
    time.sleep(5)


@Then('search electronics model')
def find_electronics(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Asus vivobook s15")
    time.sleep(10)


# Browse items by category(vehicles)
@when('click on vehicles')
def search_vehicles(context):
    vehicles = context.browser.find_element(By.XPATH, "//p[normalize-space()='Vehicles']")
    vehicles.click()
    time.sleep(5)


@Then('search vehicles model')
def find_vehicles(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Yamaha R15 v3")
    time.sleep(10)


# Browse items by category(Property)
@when('click on Property')
def search_property(context):
    Property = context.browser.find_element(By.XPATH, "//p[normalize-space()='Property']")
    Property.click()
    time.sleep(5)


@Then('search Property details')
def find_property(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Flat")
    time.sleep(10)


# Browse items by category(home & living)
@when('click on home_and_living')
def search_home_and_living(context):
    home_and_living = context.browser.find_element(By.XPATH, "//p[normalize-space()='Home & Living']")
    home_and_living.click()
    time.sleep(5)


@Then('search home_and_living')
def find_home_and_living(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("sofa")
    time.sleep(10)


# Browse items by category(home & living)
@when('click on pets_and_animals')
def search_home_and_living(context):
    home_and_living = context.browser.find_element(By.XPATH, "//p[normalize-space()='Pets & Animals']")
    home_and_living.click()
    time.sleep(5)


@Then('search pets_and_animals')
def find_home_and_living(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("kokatel bird")
    time.sleep(10)


# Browse items by category(men's fashion & grooming)
@when('click on mens_fashion_and_grooming')
def search_home_and_living(context):
    mens_fashion_and_grooming = context.browser.find_element(By.XPATH,
                                                             "//a[@href='/en/ads/bangladesh/mens-fashion']//div[@class='info--uF0qH']//p[@class='info-title--3CkVD']")
    mens_fashion_and_grooming.click()
    time.sleep(5)


@Then('search mens_fashion_and_grooming items')
def find_mens_fashion_and_grooming_items(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Rolex watch")
    time.sleep(10)


# Browse items by category(Women's fashion & beauty)
@when('click on Womens fashion beauty')
def search_Womens_fashion_and_beauty(context):
    Womens_fashion_and_beauty = context.browser.find_element(By.XPATH,
                                                             "//a[@href='/en/ads/bangladesh/womens-fashion']//div[@class='info--uF0qH']//p[@class='info-title--3CkVD']")
    Womens_fashion_and_beauty.click()
    time.sleep(5)


@Then('search Womens fashion beauty items')
def find_Womens_fashion_and_beauty(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Diamond Ring")
    time.sleep(10)


# Browse items by category(hobbies_sports_and_kids)
@when('click on hobbies,sports and kids')
def search_hobbies_sports_and_kids(context):
    hobbies_sports_and_kids = context.browser.find_element(By.XPATH, "//p[normalize-space()='Hobbies, Sports & Kids']")
    hobbies_sports_and_kids.click()
    time.sleep(5)


@Then('search hobbies,sports and kids items')
def find_hobbies_sports_and_kids(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Guitar")
    time.sleep(10)


# Browse items by category(business & industry)
@when('click on business and industry')
def search_business_and_industry(context):
    business_and_industry = context.browser.find_element(By.XPATH, "//p[normalize-space()='Business & Industry']")
    business_and_industry.click()
    time.sleep(5)


@Then('search business and industry model')
def find_business_and_industry(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("coffee machine")
    time.sleep(10)


# Browse items by category(essentials)
@when('click on essentials')
def search_essentials(context):
    essentials = context.browser.find_element(By.XPATH, "//p[normalize-space()='Essentials']")
    essentials.click()
    time.sleep(5)


@Then('search essentials items')
def find_essentials(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Oil")
    time.sleep(10)


# Browse items by category(education)
@when('click on education')
def search_education(context):
    education = context.browser.find_element(By.XPATH, "//p[normalize-space()='Education']")
    education.click()
    time.sleep(5)


@Then('search education organization')
def find_education(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Home teacher")
    time.sleep(10)


# Browse items by category(services)
@when('click on services')
def search_services(context):
    services = context.browser.find_element(By.XPATH, "//p[normalize-space()='Services']")
    services.click()
    time.sleep(5)


@Then('search services items')
def find_services(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("AC")
    time.sleep(10)


# Browse items by category(jobs)
@when('click on jobs')
def search_jobs(context):
    jobs = context.browser.find_element(By.XPATH, "//p[normalize-space()='Jobs']")
    jobs.click()
    time.sleep(5)


@Then('search jobs')
def find_jobs(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("Driver")
    time.sleep(10)


# Browse items by category(agriculture)
@when('click on agriculture')
def search_agriculture(context):
    agriculture = context.browser.find_element(By.XPATH, "//p[normalize-space()='Agriculture']")
    agriculture.click()
    time.sleep(5)


@Then('search agriculture items')
def find_agriculture(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("তেজ পাতা")
    time.sleep(10)


# Browse items by category(jobs)
@when('click on overseas jobs')
def search_overseas_jobs(context):
    overseas_jobs = context.browser.find_element(By.XPATH, "//p[normalize-space()='Overseas Jobs']")
    overseas_jobs.click()
    time.sleep(5)


@Then('search overseas jobs')
def find_overseas_jobs(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("ওয়ার্ক পারমিট")
    time.sleep(10)


# senario number 4
@Then('Click on all ads')
def click_ads(context):
    context.browser.find_element(By.XPATH, "//a[@class='all-ads-button--1c5U5 header-link--woAbP']").click()
    time.sleep(10)


@When('click on select location')
def click_location(context):
    context.browser.find_element(By.XPATH, "//button[normalize-space()='Select Location']").click()
    time.sleep(5)


@Then('click on dhaka')
def click_ads(context):
    context.browser.find_element(By.XPATH, "(//div[@class='name--4feK3']) [1]").click()
    time.sleep(5)


@When('click on mirpur')
def click_location(context):
    context.browser.find_element(By.XPATH, "(//div[@class='name--4feK3']) [20]").click()
    time.sleep(5)


@Then('select sort results by box')
def click_search_box(context):
    context.browser.find_element(By.XPATH,
                                 "//span[contains(@class,'inline-display--3Xta0 popover--3tlT1')]//span//button[@id='dd-button']").click()
    time.sleep(5)


@When('select newest on top')
def click_newest(context):
    context.browser.find_element(By.XPATH, "//li[@id='date_desc']").click()
    time.sleep(5)


@Then('select urgent')
def urgent(context):
    context.browser.find_element(By.XPATH,
                                 "//label[contains(@for,'checkbox_id_0')]//span[contains(@class,'label-text-span--2LWsk')]").click()
    time.sleep(5)


@When('select type of poster All')
def select_type(context):
    context.browser.find_element(By.XPATH,
                                 "//div[contains(@class,'poster-dropdown-wrapper--iM5gh')]//div[contains(@class,'dd-wrapper--1d8aT')]//span[contains(@class,'popover--3tlT1')]//span//button[@id='dd-button']").click()
    time.sleep(5)


@Then('click on mobiles')
def mobiles(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Mobiles']").click()
    time.sleep(5)


@When('click on mobilePhones')
def mobilephones(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Mobile Phones']").click()
    time.sleep(5)


@then('search apple in search box')
def select_box(context):
    search_box = context.browser.find_element(By.XPATH, "//input[contains(@placeholder,'What are you looking for?')]/.")
    search_box.click()
    search_box.send_keys("Apple")
    time.sleep(10)


@When('click on search button')
def search(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)


# senario number 5
@Then('click on electronics')
def electronics(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Electronics']").click()
    time.sleep(5)


@When('click on laptops')
def laptops(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Laptops']").click()
    time.sleep(5)


@then('search asus in search box')
def select_box(context):
    search_box = context.browser.find_element(By.XPATH, "//input[contains(@placeholder,'What are you looking for?')]/.")
    search_box.click()
    search_box.send_keys("asus")
    time.sleep(10)


# senario number 6
@Then('click on vehicles')
def electronics(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Vehicles']").click()
    time.sleep(5)


@When('click on motorbikes')
def laptops(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='Motorbikes']").click()
    time.sleep(5)


@then('search rtr 4v in search box')
def select_box(context):
    search_box = context.browser.find_element(By.XPATH, "//input[contains(@placeholder,'What are you looking for?')]/.")
    search_box.click()
    search_box.send_keys("rtr")
    time.sleep(5)


# senario number 7
@Then('click on bangla')
def bangla(context):
    context.browser.find_element(By.XPATH, "//button[@class='gtm-hamburger-locale']").click()
    time.sleep(5)


# senario number 8
@Then('Click on about us')
def about(context):
    context.browser.find_element(By.XPATH, "//span[normalize-space()='About Us']").click()
    time.sleep(5)


@When('sent massage on email')
def sent_email(context):
    context.browser.find_element(By.XPATH, "//a[normalize-space()='support@bikroy.com']").click()
    time.sleep(5)


# senario number 9
@Then('Click explore more')
def more(context):
    context.browser.find_element(By.XPATH, "//span[@class='pad-right--1WcbJ']").click()
    time.sleep(5)


@When('click on view all jobs')
def jobs(context):
    context.browser.find_element(By.XPATH, "//button[normalize-space()='View all jobs']").click()
    time.sleep(5)


@then('click on search box write computer')
def select_box(context):
    search_box = context.browser.find_element(By.XPATH, "//input[@placeholder='What are you looking for?']")
    search_box.click()
    search_box.send_keys("computer")
    time.sleep(5)


@When('click on search')
def search(context):
    context.browser.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
    time.sleep(10)


# senario number 10
@Then('Click on login')
def login(context):
    context.browser.find_element(By.XPATH, "//a[@aria-label='Login']").click()
    time.sleep(5)


@When('click on continue with email')
def google_login(context):
    context.browser.find_element(By.XPATH,
                                 "(//button[@class='btn--1gFez secondary--Os-e9 background--2lR9B small--1MQ15 button--eCUEQ gtm-email-login'])").click()
    time.sleep(5)


@Then('enter email')
def gmail_login(context):
    search_box = context.browser.find_element(By.XPATH, "(//input[@id='input_email'])")
    search_box.click()
    search_box.send_keys("habibswe.qups@gmail.com")
    time.sleep(5)


@When('type password')
def next(context):
    search_box = context.browser.find_element(By.XPATH, "(//input[@id='input_password'])")
    search_box.click()
    search_box.send_keys("28343215")
    time.sleep(5)


@Then('Click login button')
def login(context):
    search_box = context.browser.find_element(By.XPATH,"(//div[@class='justify-content-flex-end--jceWj align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1'])")
    search_box.click()
    time.sleep(10)


# senario number 11
@Then('Click on My account')
def account(context):
    context.browser.find_element(By.XPATH, "(//a[@class='header-link--woAbP title--1NHWk gtm-myaccount-click'])[1]").click()
    time.sleep(5)


@When('click on profile database')
def database(context):
    context.browser.find_element(By.XPATH, "//a[normalize-space()='Profile Database']").click()
    time.sleep(5)


##senario number 12

@When('click on setting')
def setting(context):
    search_box = context.browser.find_element(By.XPATH, "//a[normalize-space()='Settings']")
    search_box.click()
    time.sleep(5)


@Then('click on logout')
def login(context):
    search_box = context.browser.find_element(By.XPATH, "(//button[@class='btn--1gFez danger--AAW-T medium--51K9p']) [1]")
    search_box.click()
    time.sleep(5)

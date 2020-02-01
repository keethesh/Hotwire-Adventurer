from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import *
import re
import webbrowser

opts = Options()
opts.add_argument("--headless")
browser = Firefox(options=opts)
print("The full URL looks like \"https://www.hotwire.com/hotels/details/XXXXXXX\"")
hotwire_deal_url = input("Enter your full hotwire hot deal URL: ")
browser.get(hotwire_deal_url)

try:
    room_photo_url = browser.find_element_by_xpath("//div[@ng-class=[$ctrl.thumbnailPhotoContainer]"
                                                   "actual-room-photos__thumbnail-blur "
                                                   "actual-room-photos__thumbnail-desktop']").get_attribute("style")
except NoSuchElementException:
    room_photo_url = browser.find_element_by_xpath("//div[@class='actual-room-photos__thumbnail "
                                                   "actual-room-photos__thumbnail-desktop "
                                                   "actual-room-photos__thumbnail-blur']").get_attribute("style")

room_photo_url = re.findall(r'"([^"]*)"', room_photo_url)[0]
browser.get("https://www.google.mu/imghp?hl=en&tab=wi&ogbl")
browser.find_element_by_xpath("//div[@aria-label='Search by image']").click()
browser.find_element_by_name("image_url").send_keys(room_photo_url)
browser.find_element_by_xpath("//input[@value='Search by image']").click()
while browser.current_url == "https://www.google.mu/imghp?hl=en&tab=wi&ogbl":
    pass
print("The google image webpage will now be opened in your default browser, if this does not work, the link's below:\n" +
      browser.current_url)
try:
    webbrowser.open_new_tab(browser.current_url)
except:
    pass
browser.quit()

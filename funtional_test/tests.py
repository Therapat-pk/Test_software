from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get(self.live_server_url)

        
       
        #header_text = self.browser.find_element_by_tag_name('h1').text  
        #self.assertIn('To-Do', header_text)
        POST=self.browser.find_element_by_partial_link_text('POST')
        POST.send_keys(Keys.ENTER)

        time.sleep(1)
        
        inputbox = self.browser.find_element_by_name('x')  
        #self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item'    )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('50')  

        inputbox = self.browser.find_element_by_name('y') 
        inputbox.send_keys('50')  

        plusbox = self.browser.find_element_by_name('plus') 
        plusbox.send_keys(Keys.ENTER)
        check=self.browser.find_element_by_link_text('resuit')
        self.assertEqual(check,100)



 
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_list_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)  



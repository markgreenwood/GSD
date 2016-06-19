from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Catherine heard about a cool new online GTD app called
        # GSD (for Getting Stuff Done) and goes to check out its homepage
        self.browser.get(self.server_url)
        
        # She notices the page title and header mention GSD
        self.assertIn('GSD', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GSD', header_text)
        
        # She is invited to enter a task right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a task')
        
        # She types "Buy groceries" into a text box
        inputbox.send_keys('Buy groceries')
        
        # When she hits enter, she is taken to a new URL, and now the page lists 
        # "1: Buy groceries" as an item in a task list
        inputbox.send_keys(Keys.ENTER)
        catherine_list_url = self.browser.current_url
        self.assertRegex(catherine_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy groceries')
        
        # There is still a text box inviting her to add another item.
        # She enters "Plan trip to Virginia Tech" (Catherine is a college
        # recruiter for her company)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Plan trip to Virginia Tech')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy groceries')
        self.check_for_row_in_list_table('2: Plan trip to Virginia Tech')

        # Now a new user, Thorsten, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Catherine's is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Thorsten visits the home page. There is no sign of Catherine's list.
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy groceries', page_text)
        self.assertNotIn('Plan trip to Virginia Tech', page_text)

        # Thorsten starts a new list by entering a new item. He has more Product
        # Engineering tasks than Catherine...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Write wafer mapping software')
        inputbox.send_keys(Keys.ENTER)

        # Thorsten gets his own unique URL
        thorsten_list_url = self.browser.current_url
        self.assertRegex(thorsten_list_url, '/lists/.+')
        self.assertNotEqual(thorsten_list_url, catherine_list_url)

        # Again, there is no trace of Catherine's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy groceries', page_text)
        self.assertIn('Write wafer mapping software', page_text)
        
        # Satisfied, they both go back to sleep.

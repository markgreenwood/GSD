from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Catherine heard about a cool new online GTD app called
        # GSD (for Getting Stuff Done) and goes to check out its homepage
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention GSD
        self.assertIn('GSD', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GSD', header_text)
        
        # She is invited to enter a task right away
        inputbox = self.browser.find_element_by_id('id_new_task')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a task')
        
        # She types "Buy groceries" into a text box
        inputbox.send_keys('Buy groceries')
        
        # When she hits enter, the page updates, and now the page lists 
        # "1: Buy groceries" as an item in a task list
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy groceries', [row.text for row in rows])
        
        # There is still a text box inviting her to add another item.
        # She enters "Plan trip to Virginia Tech" (Catherine is a college
        # recruiter for her company)
        inputbox = self.browser.find_element_by_id('id_new_task')
        inputbox.send_keys('Plan trip to Virginia Tech')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy groceries', [row.text for row in rows])
        self.assertIn('2: Plan trip to Virginia Tech', [row.text for row in
            rows])
        
        # Catherine wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        self.fail('Finish the test!')
        
        # She visits that URL - her task list is still there.
        
        # Satisfied, she goes to sleep.

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')

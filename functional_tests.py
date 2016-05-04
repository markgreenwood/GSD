from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Catherine heard about a cool new online GTD app and
        # goes to check out its homepage
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention GTD
        self.assertIn('GTD', self.browser.title)
        self.fail('Finish the test!')
        
        # She is invited to enter a task right away
        
        # She types "Buy groceries" into a text box
        
        # When she hits enter, the page updates, and now the page lists 
        # "1: Buy groceries" as an item in a task list
        
        # There is still a text box inviting her to add another item.
        # She enters "Plan trip to Virginia Tech" (Catherine is a college
        # recruiter for her company)
        
        # The page updates again, and now shows both items on her list
        
        # Catherine wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        # She visits that URL - her task list is still there.
        
        # Satisfied, she goes to sleep.

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path = '/home/bart/web_dj_sample/TDD_WEB_DJANGO/geckodriver')
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Eds heard that there is a online to-do list App which is cool.
        #Eds go home page of the App.
        self.browser.get('http://localhost:8000')
        #Eds notice that both title and header of the web page consist of word 'To-DO'. 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_elements_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #The App ask she to provide a input which is a to-do envent.
        inputbox = self.brower.find_element_by_tag_id('id_new_item')
        self.asserrEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #She type in a textbox which is 'Bug peacock feathers'
        #Eds like make fishing by fly
        inputbox.send_keys('Buy peacock feathers')
        
        #She press enter, page refreshed.
        #to-do list shows '1: Bug peacock feathers'.
        inputbox.send_keys(Keys.ENTER)
        table = self.brower.find_element_by_tag_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTure(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )   
        #another textbox shown so that she can input other to-dos.
        #she types 'Use peacock feathers to make a fly'
        #Eds do things in orders.
        self.fail('Finish The Test!')
        #Home page is refreshed again and there are two to-dos in the list.
        #Eds wants to know if the App can remmenber her list.
        #she find that the App has generate a unique URL for her.
        #There are some words to describe the functiona of the App.
        #She access the App again by the URL and her to-do list is still there.
        #she feels good and go to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    





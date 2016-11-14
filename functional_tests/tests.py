from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.test import LiveServerTestCase

class NewVistorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path = '/home/bart/web_dj_sample/TDD_WEB_DJANGO/geckodriver')
        self.browser.implicitly_wait(0)
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        time.sleep(0)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Eds heard that there is a online to-do list App which is cool.
        #Eds go home page of the App.
        self.browser.get(self.live_server_url)
        #Eds notice that both title and header of the web page consist of word 'To-DO'. 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #The App ask she to provide a input which is a to-do envent.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #She type in a textbox which is 'Bug peacock feathers'
        #Eds like make fishing by fly
        inputbox.send_keys('Buy peacock feathers')
        
        #She press enter and be redirected to another URL.
        #to-do list in the new page shows '1: Bug peacock feathers'.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')  
        #another textbox shown so that she can input other to-dos.
        #she types 'Use peacock feathers to make a fly'
        #Eds do things in orders.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)        
        #Home page is refreshed again and there are two to-dos in the list.
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        time.sleep(1)
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # now there is a new user access to the site whoes name is Frances
        ## we use a new browser session
        ## to ensure edith's data will not leak from cookie
        self.browser.quit()
        time.sleep(1)
        self.browser = webdriver.Firefox(executable_path = '/home/bart/web_dj_sample/TDD_WEB_DJANGO/geckodriver')
        # Frances access the HomePage
        # Edith's list is not there
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        #Frances enter a new to-do and create a new lists
        #he doesn't feel cool.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #Frances get his unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        #this page contains no edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        #They both feel good and go to sleep then
        self.fail('Finish The Test!')


    
    





from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    
    def setUp(self):
        self.brower = webdriver.Firefox(executable_path = '/home/bart/web_dj_sample/TDD_WEB_DJANGO/geckodriver')
        self.brower.implicitly_wait(3)
        
    def tearDown(self):
        self.brower.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Eds heard that there is a online to-do list App which is cool.
        #Eds go home page of the App.
        self.brower.get('http://localhost:8000')
        #Eds notice that both title and header of the web page consist of word 'To-DO'. 
        self.assertIn('To-Do', self.brower.title)
        self.fail('Finish The Test!')

#The App want she provide a input which is a to-do envent.

#She type in a textbox which is 'Bug peacock feathers'

#Eds like make fishing by fly

#She press enter, page refreshed.

#to-do list shows 'Bug peacock feathers'.

#another textbox shown so that she can input other to-dos.

#she types 'Use peacock feathers to make a fly'

#Eds do things in orders.

#Home page is refreshed again and there are two to-dos in the list.

#Eds wants to know if the App can remmenber her list.

#she find that the App has generate a unique URL for her.

#There are some words to describe the functiona of the App.

#She access the App again by the URL and her to-do list is still there.

#she feels good and go to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    





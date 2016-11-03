from selenium import webdriver
brower = webdriver.Firefox(executable_path = '/home/bart/web_dj_sample/TDD_WEB_DJANGO/geckodriver')
brower.get('http://localhost:8000')
#http://localhost:8000
assert 'Django' in brower.title


from selenium import webdriver # http://pythonclub.com.br/selenium-parte-1.html
from selenium.webdriver.common.keys import Keys # https://stackoverflow.com/questions/1629053/typing-enter-return-key-in-selenium
import time # https://www.tutorialspoint.com/python/time_sleep
from selenium.webdriver.common.by import By # https://selenium-python.readthedocs.io/waits.html#explicit-waits 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

author_name = "Jeffrey Heer"

# Iniciando o Selenium
wd = webdriver.Firefox(executable_path = "C:/Users/LuizFernando/Documents/GitHub/FDS-Homeworks/hw1/geckodriver.exe") # https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
# Existe algo similar a um Rproject?

# Indo para página
wd.get("https://scholar.google.com.br/")

# Pesquisando pelo nome do autor
WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gs_hdr_tsi")))
search_box = wd.find_element_by_css_selector("#gs_hdr_tsi")
search_box.send_keys(author_name)
search_box.send_keys(Keys.ENTER)

# Clicando no primeiro perfil
WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gs_r")))
profile = wd.find_element_by_css_selector(".gs_rt2 b") 
profile.click()

# Clicando no mostrar mais até que não dê mais
page, new_page = "1", "2"
while page != new_page:
    time.sleep(0.5)
    page = wd.page_source
    mostrar_mais = wd.find_element_by_css_selector("#gsc_bpf_more .gs_wr") 
    mostrar_mais.click()
    new_page = wd.page_source
   
# Coletando os títulos e autores
title = []
authors = []

we = wd.find_elements_by_css_selector(".gsc_a_at")
for i in we:
    title.append(i.text)

we = wd.find_elements_by_css_selector(".gsc_a_at+ .gs_gray")
for i in we:
    authors.append(i.text.split(", "))
    
# Finalizando o Selenium
wd.quit()


len(title)
len(authors)




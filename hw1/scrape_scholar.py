from selenium import webdriver # http://pythonclub.com.br/selenium-parte-1.html
from selenium.webdriver.common.keys import Keys # https://stackoverflow.com/questions/1629053/typing-enter-return-key-in-selenium
from selenium.webdriver.common.by import By # https://selenium-python.readthedocs.io/waits.html#explicit-waits 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time # https://www.tutorialspoint.com/python/time_sleep

def scrape(author_name):
    
    # Iniciando o Selenium e indo até a página
    wd = webdriver.Firefox(executable_path = "./geckodriver.exe") # https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
    wd.get("https://scholar.google.com.br/")
        
    # Pesquisando pelo nome do autor
    WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gs_hdr_tsi")))
    search_box = wd.find_element_by_css_selector("#gs_hdr_tsi")
    search_box.send_keys(author_name)
    search_box.send_keys(Keys.ENTER)
    
    # Clicando no primeiro perfil
    WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gs_r")))
    
    try:
        profile = wd.find_element_by_css_selector(".gs_rt2 b") 
        profile.click()
    except:
        wd.quit()
        print("Autor não encontrado.")
        return None
        
    # Clicando no mostrar mais até que não dê mais
    page, new_page = "", wd.page_source
    while page != new_page:
        time.sleep(0.5)
        page = new_page
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
        authors.append(list(filter(lambda x: x != "...", i.text.split(", ")))) # https://www.geeksforgeeks.org/python-ways-to-remove-particular-list-element/
     
    # Finalizando o Selenium e arrumando o output
    wd.quit()
    output = []
    for i in range(len(title)):
        output.append({"title": title[i], "authors": authors[i]})
        
    return output
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
//
# Setup: Configuração do WebDriver
options = Options()

# Executa o navegador em modo invisível, opcional
#options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
 

# Setup: Caminho do ChromeDriver
service = Service('C:\\chromedriver\\chromedriver.exe')

# Setup: Inicializar o navegador
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

try:
    # PASSO 1) Acessar a URL do site de login
    print("Passo 1 -  Acessar a URL do site ========INICIO=======")
    driver.get("https://app.anchieta.br/Anchieta_Instructure_Canvas/Login.php")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usuario")))
    print("Passo 1 -  Acessar a URL do site *****SUCESSO*******")


    # PASSO 2) Preencher o campo de RA
    print("Passo 2 -  Preencher o campo de RA ========INICIO=======")
    ra_input = driver.find_element(By.ID, "usuario")
    ra_input.send_keys("INSERIR RA AQUI!!")
    print("Passo 2 -  Preencher o campo de RA *****SUCESSO*******")


    # PASSO 3) Preencher o campo de senha
    print("Passo 3 -  Preencher o campo de senha ========INICIO=======")
    senha_input = driver.find_element(By.ID, "senha")
    senha_input.send_keys("INSERIR SENHA AQUI!!*")
    print("Passo 3 -  Preencher o campo de senha *****SUCESSO*******")


    # PASSO 4) Efetuar login
    print("Passo 4 - Efetuar o Login ========INICIO=======")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button_login")))
    login_button.click()
    time.sleep(3)
    print("Passo 4 - Efetuar o Login *****SUCESSO*******")


    # PASSO 5) Fechar o tour
    print("Passo 5 - Fechar o tour ========INICIO=======")
    tour_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-75zwwy-view--inlineBlock-baseButton")))
    tour_button.click()
    time.sleep(3)
    print("Passo 5 - Fechar o tour *****SUCESSO*******")


    # PASSO 6) Fechar o feito
    print("Passo 6 - Fechar o feito ========INICIO=======")
    feito_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1iimhyf-view--inlineBlock-baseButton")))
    feito_button.click()
    time.sleep(3)
    print("Passo 6 - Fechar o feito *****SUCESSO*******")
 
 
    # PASSO 7) Acessar o curso
    print("Passo 7 - Acessar o curso ========INICIO=======")
    curso = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "PROJETO INTEGRADOR (EAD-ADS-PI-8-74)")))
    curso.click()
    time.sleep(3)
    print("Passo 7 - Acessar o curso *****SUCESSO*******")

    
    # PASSO 8) Clicar em conta
    print("Passo 8 - Clicar em conta ========INICIO=======")
    conta_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "ic-app-header__menu-list-link")))
    conta_button.click()
    time.sleep(3)
    print("Passo 8 - Clicar em conta *****SUCESSO*******")


    # PASSO 9) Clicar em sair
    print("Passo 9 - Clicar em sair ========INICIO=======")
    sair_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1hqqcdr-view--inlineBlock-baseButton")))
    sair_button.click()
    time.sleep(3)
    print("Passo 9 - Clicar em sair *****SUCESSO*******")
   
finally:
    # Fecha o navegador
    driver.quit()



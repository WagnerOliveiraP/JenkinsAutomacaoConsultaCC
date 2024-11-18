import logging
import time
import pandas as pd
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurar o teste
logging.basicConfig(filename='automacao.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        logging.info("Driver iniciado com sucesso.")
        return driver
    except Exception as e:
        logging.error("Erro ao iniciar o driver: " + str(e))
        logging.error(traceback.format_exc())

def buscar_produto(driver, produto):
    try:
        driver.get('https://www.mercadolivre.com.br')
        search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'cb1-edit')))
        search_box.send_keys(produto)
        search_box.submit()
        time.sleep(5)
        logging.info(f"Busca realizada com sucesso para o produto: {produto}")
    except Exception as e:
        logging.error("Erro ao buscar o produto: " + str(e))
        logging.error(traceback.format_exc())

def coletar_anuncios(driver):
    anuncios = []
    try:
        results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'ui-search-layout__item')]")))
        for idx, result in enumerate(results):
            try:
                titulo = result.find_element(By.XPATH, ".//h2").text
                preco_elemento = result.find_element(By.CLASS_NAME, "andes-money-amount__fraction")
                preco = preco_elemento.text.replace('.', '')
                link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                anuncios.append({'Anuncio': f'Anuncio {idx+1}', 'Titulo': titulo, 'Preco': preco, 'Link': link})
                logging.info(f"Anuncio {idx+1} extraído com sucesso.")
            except Exception as e:
                logging.error(f"Erro ao extrair dados do anúncio {idx+1}: {e}")
                logging.error(traceback.format_exc())
        return anuncios
    except Exception as e:
        logging.error("Erro ao coletar os anúncios: " + str(e))
        logging.error(traceback.format_exc())

def processar_anuncios(anuncios):
    try:
        df = pd.DataFrame(anuncios)
        df['Preco'] = pd.to_numeric(df['Preco'].apply(lambda x: x.replace(',', '.')), errors='coerce')
        df = df.sort_values(by='Preco').head(3)
        df['Ranking'] = range(1, len(df) + 1)
        logging.info("Anúncios processados e classificados.")
        return df
    except Exception as e:
        logging.error("Erro ao processar os anúncios: " + str(e))
        logging.error(traceback.format_exc())

def abrir_top3(driver, df_top3):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Defina um tempo máximo de espera (por exemplo, 10 segundos)
        wait = WebDriverWait(driver, 10)

        # Abrir links dos top 3 anúncios
        for link in df_top3['Link']:
            # Abrir o link em uma nova aba
            driver.execute_script(f"window.open('{link}', '_blank');")

        # Exibir uma mensagem para o usuário enquanto as abas estão abertas
        print("Os links dos top 3 anúncios foram abertos em novas abas. Feche manualmente a janela do navegador para encerrar o script.")

        # Pausar o script para que o navegador permaneça aberto até o usuário fechá-lo
        driver.switch_to.window(driver.window_handles[0])  # Focar na primeira aba
        driver.maximize_window()
        time.sleep(40)
        # Fechar o navegador ao encerrar o script
        driver.quit()
        logging.info("Top 3 anúncios abertos em novas abas.")
    except Exception as e:
        logging.error("Erro ao abrir links dos top 3 anúncios: " + str(e))
        logging.error(traceback.format_exc())

def main():
    driver = iniciar_driver()
    if driver:
        buscar_produto(driver, 'Nintendo Switch')
        anuncios = coletar_anuncios(driver)
        if anuncios:
            df_top3 = processar_anuncios(anuncios)
            abrir_top3(driver, df_top3)
            logging.info("Processo concluído.")
        else:
            logging.warning("Nenhum anúncio foi coletado.")
        driver.quit()

if __name__ == "__main__":
    main()

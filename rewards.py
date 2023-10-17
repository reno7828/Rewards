import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as noElement
from selenium.webdriver.chrome.options import Options
from tkinter import Tk, filedialog


def choose_chromedriver():
    root = Tk()
    root.withdraw()  # Masquer la fenêtre principale de tkinter

    # Ouvrir une boîte de dialogue pour choisir le chemin du ChromeDriver
    file_path = filedialog.askopenfilename(title="Sélectionnez ChromeDriver")

    if file_path:
        root.destroy()  # Fermer la fenêtre tkinter

        emails = input('Entrez vos emails séparés par des virgules (Si plusieurs mails...) : ')
        email_list = emails.split(',')
        mdp1 = input('Entrez votre mot de passe : ')

        mdp = str(mdp1)
        print('Mot de passe :', mdp)

        def motAleatoire():
            caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
            longueur = 8
            motgenerer = ""
            compteur = 0

            while compteur < longueur:
                lettre = caracteres[random.randint(0, len(caracteres) - 1)]
                motgenerer += lettre
                compteur += 1
            return motgenerer

        def delay():
            time_random = random.randint(2, 7)
            delais = time.sleep(time_random)

        def url1(mail, mdpenter):
            # # definir les urls
            # # connection a bing
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            url1 = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252fsearch%253fq%253dreno.oriou%252540live.fr%2526search%253d%2526form%253dQBLH%2526wlexpsignin%253d1%26sig%3d1095977C571C69F33707878356A568F9&wp=MBI_SSL&lc=1036&CSRFToken=9dbffcb9-e950-4a5c-8ab4-61b81ad7ec62&aadredir=1"

            chrome_service = webdriver.chrome.service.Service(file_path)
            # Passer le chemin du ChromeDriver comme argument executable_path ici
            driver1 = webdriver.Chrome(service=chrome_service, options=chrome_options)
            # driver1 = webdriver.Chrome(executable_path=file_path, options=chrome_options)

            for email in mail:
                driver1.get(url1)
                driver1.implicitly_wait(5)

                webdriver.ActionChains(driver1).send_keys(email).perform()
                webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()
                print('Email envoyé')

                delay()
                delay()

                webdriver.ActionChains(driver1).send_keys(mdpenter).perform()
                webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()
                print('Mot de passe envoyé')

                delay()

                webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()
                delay()
                webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()
                print('Enter envoyé')

                try:
                    delay()
                    accept = "#bnp_btn_accept > a"
                    print("On a appuyé sur accept")

                    clicAccept = driver1.find_element(By.CSS_SELECTOR, accept)
                    delay()
                    clicAccept.click()
                    delay()
                except:
                    searBar = '//*[@id="sb_form_q"]'
                    clicSearch = driver1.find_element(By.XPATH, searBar)
                    clicSearch.click()
                    print("Clicsearch ok")
                    clicSearch.clear()
                    print('Clicsearch erase')
                    delay()
                    clicSearch.click()
                    print("Clicsearch clic")

                mots = motAleatoire()
                webdriver.ActionChains(driver1).send_keys(motAleatoire()).perform()
                webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()

                delay()

                try:
                    clicok = "bnp_btn_accept"
                    clicokAccept = driver1.find_element(By.ID, clicok)
                    clicokAccept.click()
                except:
                    pass

                i = 0
                b = random.randint(50, 57)




                while i < b:
                    mots = motAleatoire()
                    webdriver.ActionChains(driver1).send_keys(motAleatoire()).perform()
                    webdriver.ActionChains(driver1).send_keys(Keys.ENTER).perform()
                    delay()
                    delay()
                    searBar = '//*[@id="sb_form_q"]'
                    clicSearch = driver1.find_element(By.XPATH, searBar)
                    clicSearch.click()
                    clicSearch.clear()
                    clicSearch.click()

                    i += 1
                    print("Il reste :", b - i, "tours")
                    delay()
                    delay()

            driver1.quit()


        while True:
            try:
                print('Go Rewards')

                url1(email_list, mdp)
                print('Recherches terminées...')
                delay()

            except noElement:
                pass
            break
    else:
        root.destroy()  # Fermer la fenêtre tkinter si l'utilisateur annule


choose_chromedriver()

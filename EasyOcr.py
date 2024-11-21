from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import easyocr
# reader = easyocr.Reader(lang_list=['af', 'sq', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'yue', 'ca', 'hr', 'cs', 'da', 'prs', 'nl', 'en', 'et', 'fj', 'fil', 'fi', 'fr', 'de', 'el', 'gu', 'ht', 'he', 'hi', 'mww', 'hu', 'is', 'id', 'it', 'ja', 'kn', 'kk', 'tlh', 'tlh-Qaak', 'ko', 'ku', 'ky', 'lo', 'lv', 'lt', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'nb', 'ne', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'otq', 'ro', 'ru', 'sm', 'sr-Cyrl', 'sr-Latn', 'sk', 'sl', 'es', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'xh', 'yi', 'yua', 'zu'])
reader=easyocr.Reader(lang_list=["sq","en","es",'pt', 'tr','af'],gpu=False)

path='image2.png'
file_path = os.path.abspath(path)
print(file_path)


def apply_ocr():
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://lens.google.com/search?p")

        # Gjej elementin duke përdorur emrin e klases
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        element.click()

        try:
            menu_item_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "amqM1")))
            time.sleep(1)
            menu_item_element.click()

            try:
                driver.find_element(By.XPATH, "//input[@type='file']")
                print('Comp input found')
            except:
                print('Computer item not found.')

            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
                file_path)

            text_ = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ucj-2']")))
            print('Text Found')
            text_.click()

            select_all_text = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/button")))

            select_all_text.click()
            print('Select all text clicked')

            all_text = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                       "//*[@id='yDmH0d']/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/span/div/h1")))

            text_str = all_text.text
            driver.quit()
            return text_str




        except:
            print('An error ocurred')
            return None


def from_easy_ocr():
    allowlist=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ë','ç', 'á', 'ã', 'â', 'à', 'é', 'ê', 'í', 'ó', 'õ', 'ô', 'ú',
               'à', 'â', 'ç', 'é', 'è', 'ê', 'î', 'ï', 'ô', 'û', 'ù','ì', 'ò', 'ù','ı','ğ','ü',
               'ü','ş','ö', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و',
               'ا','ي','अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह',
               '的', '一', '是', '不', '了', '在', '人', '有', '我', '他', '这', '个', '们', '中', '大', '来', '上',
               '国', '个', '们', '中', '大', '来', '上', '国'
               ]
    # Nxirr tekstin nga fotografia
    result =reader.readtext(file_path,decoder='wordbeamsearch',batch_size=2,paragraph=True,min_size=2,contrast_ths=0.05,
                    canvas_size=4000,text_threshold=0.55,adjust_contrast=0.7)  # Krijo një string për të mbledhur tekstin
    full_text = ""

    # Shto tekstin e deteksionit në string
    for detection in result:
       full_text += detection[1] + " "

    # Printo të gjithë tekstin
    return full_text
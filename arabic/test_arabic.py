from direct_quotes import replace

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def web_obj_config():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.use_chromium = True # if we use Edge browser
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return options

def text_extract(web_obj, url):
    web_obj.get(url)
    result = web_obj.find_elements(By.CSS_SELECTOR, 'div[class="cont"] p')
    for r in result:
        yield r.text
    # return len(result)

def main():
    chrome_path = Service("./chromedriver.exe")
    options = web_obj_config()
    web_obj = webdriver.Chrome(service=chrome_path, options=options)
    url = 'http://arabic.news.cn/2022-02/21/c_1310481775.htm'

    extracted_arabic = text_extract(web_obj, url)

    log = []

    while True:
        try:
            arabic_text = next(extracted_arabic)
            # print('--> original text: {} '.format(arabic_text))
            # print('--> remove quotes: {}'.format(replace(arabic_text)))
            # print('----------------------------------------------------')
            ori = arabic_text
            remove = replace(arabic_text)
            log.append(ori)
            log.append(remove)
            log.append('----------------------------------------------------')

        except:
            with open('test_result.txt', 'w', encoding='utf-8') as fwrite:
                fwrite.write('\n'.join(log))
            web_obj.quit()
            break

if __name__ == '__main__':
    main()

    
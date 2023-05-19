from datetime import date
from subprocess import check_call
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

options = webdriver.ChromeOptions()
s = Service('chromedriver/chromedriver96.exe')
driver = webdriver.Chrome(service=s, options=options)

rate = 0
driver.get("https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.find_all("div", {"class": "embed-rate"}):
    txt=a.find('span').text
    rate = float(re.findall(r'[\d]*[.][\d]+',txt)[0])
    print(rate)

driver.close()
driver.quit()

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)

def calculate(uplata):
    mirI = 0.075*uplata
    mirII = 0.025*uplata
    osnovica = uplata - mirI - mirII
    uk_mir = mirI + mirII
    porez = 0.2*osnovica
    za_isplatu = osnovica - porez
    ispis = [mirI, mirII, uk_mir, osnovica, porez, za_isplatu]
    print("upisi datum u zaglavlje\n")
    print("prvo A\n")
    stavi_i_cekaj(porez)
    for i in range(2):
        stavi_i_cekaj(ispis[i],i)

    print("sad B; iznos (oporezivi) x2\n")
    stavi_i_cekaj(uplata,"",True)
    for i in range(len(ispis)):
        if i==3:
            stavi_i_cekaj(ispis[i], i, True)
        else:
            stavi_i_cekaj(ispis[i], i)
    print(ispis)


def stavi_i_cekaj(inp, i="", d=False):
    copy2clip(str(round(inp,2)).replace(".", ","))
    if d:
        z=input("x2\n")
    else:
        z=input()

print("23"+"{0:0=3d}".format(date.today().timetuple()[7]))
if input("potvrdi tecaj: upisi 'n' za poništavanje  ").lower() == "n":
    rate = float(input("1 EUR = ... USD s decimalnom tockom  "))
uplataUSD = float(input("u USD  ").replace(",", "."))
uplataEUR = round(uplataUSD/rate, 2)

calculate(uplataEUR)

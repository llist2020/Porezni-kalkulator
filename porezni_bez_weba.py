from datetime import date
from subprocess import check_call


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
uplataUSD = float(input("u USD  ").replace(",", "."))
tecaj = float(input("1 EUR = ... USD s tockom  "))
uplataEUR = round(uplataUSD/tecaj, 2)

calculate(uplataEUR)

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
req = Request('https://www.bauruempregos.com.br/home/vagas', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)#.read()
#html=urlopen('https://www.bauruempregos.com.br/home/vagas') nao funciona ocorre erro 403
#print(html.read())
soup=BeautifulSoup(html.read(),'html.parser')
vagas=soup.find_all("div", class_=["vaga","data-vagas"])
datas={}
dictname=""
for item in vagas:
    #print(item)
    if item.a: #verifica se a existe dentro da div se existir nao é o nome da vaga 
        nomevaga=str(item.a.string).strip()
        if "[ANÚNCIO ENCERRADO]" not in nomevaga:
            #vagas.pop(item)
            print(nomevaga)
            datas[dictname].append(nomevaga)
        #else:
        #    print (nomevaga)
    else:
        print("\n ---------------------------\n")
        print(f"ITENS DO DIA {item.string} ")
        print("\n ---------------------------\n")
        dictname=item.string
        datas[dictname]=[]
    #Filtra todos os anuncios que estao encerrados ^
print(datas)
print("----------")
print(datas['31/07/2021'])
    #else:
    #    print(nomevaga)
    #    print("mudar aqui")

    #import csv
    #arquivo=open("bauruempregos.csv","w")
    #arquivo.close()
final_data=[]    
for dia,vagas in datas.items():
    for vaga in vagas:
        final_data.append([vaga,dia])
data_frame = pd.DataFrame.from_dict(final_data) 
data_frame.to_csv (r'dados.csv', index = False, header=False)

#!/usr/bin/python3
# lang pt-br
# author: postcristiano

import time, sys

def menu():
    try:
        enlc = 0
        opcao = int(input('''
//========================================================\\\\
||                     Contador de CN                     ||
|]========================================================[|
|| -=> [1] - Fornecer OMs apoiadas                        ||
|| -=> [2] - Fornecer quantidade de ligações necessárias  ||
|| -=> [3] - Sair..                                       ||
\\\========================================================//

        ..selecione uma opção: '''))
        if opcao == 1:
            a = int(input("Quantas Bda da DE existem (não contar em reserva) ? "))
            b = int(input("Quantas Bda da DE existem em reserva ? "))
            c = str(input("O Gpt Log está presente e vai ser ligado ao SCA [S/N] ? "))
            if c == "S" or "s":
                c = 2
            elif c == "N" or "n":
                c = 0
            else:
                print("Selecione apenas opções válidas..")
                time.sleep(2)
                menu()
            d = int(input("Quantos Enlaces de Rede são necessários para atender ligaçoes com outras GU (não contabilizar justapostas) ? "))
            e = 2 # enlaces do CN futuro
            enlc = 2 * (a + b + c + d + e)
            pass
        elif opcao == 2:
            enlc = int(input("Quantas são as ligações necessarias? \n"))
            pass
        elif opcao == 3:
            sys.exit()
        else:
            print("[-] Opção inválida.. Tente novamente :D.\n")
            menu()
        
        if enlc <= 0:
            print("[-] Opção inválida..")
        elif 0 < enlc <= 20:
            print("A quantidade de CNs p/ seu sistema Nodal é 4")
        else:
            cn =  int(enlc / 5)
            if enlc % 10 != 0:
                cn += 1
                print(f"A quantidade de CNs p/ seu sistema Nodal é {cn}")
            else:
                print(f"A quantidade de CNs p/ seu SCA é {cn}")

    except Exception as e:
        print ("[-] Opção inválida. Vamos tentar denovo.. %s\n"%e)
        menu()

    except KeyboardInterrupt:
        sys.exit()

menu()


























"""

Total_CN_BCom = 8
CN_Reserva_BCom = 2 #imposicao
CN_Futuro = 1 #imposicao

Total_CN_BCom -= (CN_Reserva_BCom  + CN_Futuro)


CN_Livres = Total_CN_BCom
CCom_DE_NA = 2
CCom_DE_Altn_NA = 2
Enlc_CN_Futuro_NA = 2

#CN_Livres -= (CCom_DE + CCom_DE_Altn)
Total_NA = 0
Total_NA += CCom_DE_NA + CCom_DE_Altn_NA
#print(Total_NA)

#SOMA DOS ENLACES
try:
    CCom_Bda_NA = int(input("Quantas Brigadas possui a DE apoiada? "))
    Total_NA += 2*CCom_Bda_NA
    CCom_OM_Org_NA = int(input("Quantas elementos de apoio orgânicos à DE possui (ex: PC AD , PC Gpt E, PC Cmdo Log que desdobra a BLB )? "))
    Total_NA += CCom_OM_Org_NA
    CCom_OM_Org_Altn_NA = int(input("Quantas elementos de apoio orgânicos a DE apoiada necessitam de ligações exclusivas para seus PC Altn? "))
    Total_NA += CCom_OM_Org_Altn_NA
    CCom_Exc_NA = int(input("Quantas Unidades Diretamente Subordinadas, EXCEPCIONALMENTE, precisão de ligação? "))
    Total_NA += CCom_Exc_NA
    CCom_Bda_Res_NA = int(input("Quantas Brigadas em RESERVA possui a DE apoiada? "))
    Total_NA += CCom_Bda_Res_NA
except ValueError:
        print("Parabens, vc conseguiu ser limitado o suficiente para nao conseguir usar este script merda de maneira correta, faça um favor pra sociedade e se afogue na sua privada!!")


#y_par = 5*x
#y_impar = 5*x - 1

# 4 CN
min_enlace_rede = 3

if Total_NA <= 20:
    CN = 4
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
elif 20 < Total_CN_BCom <=24:
    CN = 5
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
elif 24 < Total_CN_BCom <=30:
    CN = 6
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
elif 30 < Total_CN_BCom <=34:
    CN = 7
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
elif 34 < Total_CN_BCom <= 40:
    CN = 8
    print("Pode ser o caso você revisar seu planejamento, você esta necessitando de mais recursos do que o previso no B Com")
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
elif 40 < Total_CN_BCom <= 44:
    CN = 9
    print("Pode ser o caso você revisar seu planejamento, você esta necessitando de mais recursos do que o previso no B Com")
    print(f"O seu SCA será composto por {CN} Centros Nodais interligados entre si através de {min_enlace_rede*CN} enlaces de rede que interligam os elementos através de {Total_NA} enlances de junção ")
else:
    print("porra.. nao fode !")

    


# 5 CN

# 6 CN

# 7 CN

# 8 CN

# 9 CN

# 10 CN

    
#print(Total_NA)







"""

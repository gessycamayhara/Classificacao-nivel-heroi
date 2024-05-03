nome = input("Olá, por favor, insira seu nome: ")
XP = int(input("Insira a quantidade de XP: "))

if XP >=0 and XP < 1000:
    print(f"O Herói de nome {nome} está no nível Ferro")

elif XP >= 1001 and XP <= 2000:
    print(f"O Herói de nome {nome} está no nível Bronze")

elif XP >= 2001 and XP <= 5000:
    print(f"O Herói de nome {nome} está no nível Prata")    

elif XP >= 5001 and XP <= 7000:
    print(f"O Herói de nome {nome} está no nível Ouro")
    
elif XP >= 7001 and XP <= 8000:
    print(f"O Herói de nome {nome} está no nível Platina")
    
elif XP >= 8001 and XP <= 9000:
    print(f"O Herói de nome {nome} está no nível Ascendente")  
    
elif XP >= 9001 and XP <= 10000:
    print(f"O Herói de nome {nome} está no nível Imortal")    
    
elif XP > 10000:
    print(f"O Herói de nome {nome} está no nível Radiante")    

else:
    print("Insira um XP válido!")       
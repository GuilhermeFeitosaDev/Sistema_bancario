menu = """
_________GH_BANK_________
           
    (1)Depositar
    (2)Sacar
    (3)Extrato
    (0)sair 

_________GH_BANK_________  
        
"""

saldo = 0 
limite = 1000
extrato = ""
numero_saques = 0
limite_saques = 5

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar:"))

        if valor>0:
          saldo += valor
          extrato +=f"deposito: R${valor:.2f}\n"
    
        else:
            print("Operação falhou! O valor informado é invalido")

   
    elif opcao == "2":
        valor = float(input("informe o valor que deseja sacar:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques >= limite_saques 

        saque = valor < limite 

        if excedeu_saldo:
            print("Operação falhou! voce não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")

        elif excedeu_saques:
            print("Operação falhou! Voce excedeu o limite de saque diarios")

        elif valor > 0: 
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1 

        else:
            print("Operação falhou! O valor informado é invalido.")

 
 
    elif opcao =="3":
        print("\n======= EXTRATO=======")
        print( "Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo:R$ {saldo:.2f}")
        print("======================")

    elif opcao =="0":
        print("Obrigado por usar nossos serviços !! ")
        break












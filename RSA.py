from sympy import isprime
import math
import random

print("1 - Inserir p e q manualmente")
print("2 - Gerar p e q aleatórios")
op = input("Opção: ")

if op == '2':
    p = random.randint(17, 999)
    while isprime(p) == False:
        p = random.randint(17, 999)
        
    q = random.randint(17, 999)
    while isprime(q) == False or q == p:
        q = random.randint(17, 999)
        
    print("Primo p gerado:", p)
    print("Primo q gerado:", q)
    n = p * q

else:
    p = int(input('Informe um número primo: '))
    while isprime(p) == False:
        p = int(input('Informe um número primo: '))

    q = int(input('Informe outro número primo: '))
    while isprime(q) == False or q == p:
        q = int(input('Informe outro número primo: '))

    n = p * q

    while n <= 233:
        print("O seu N resultou em", n)
        print("O N precisa ser maior que 233 para não cortar os caracteres.")
        
        p = int(input('Informe um novo número primo: '))
        while isprime(p) == False:
            p = int(input('Informe um novo número primo: '))

        q = int(input('Informe outro número primo: '))
        while isprime(q) == False or q == p:
            q = int(input('Informe outro número primo: '))
            
        n = p * q

z = (p - 1) * (q - 1)

d = int(input("Insira um número sem divisores comuns com " + str(z) + ": "))

while math.gcd(d, z) != 1:
    print("Valor inválido! O número " + str(d) + " e " + str(z) + " possuem divisores em comum.")
    d = int(input("Insira um número sem divisores comuns com " + str(z) + ": "))

e = pow(d, -1, z)

print("\nChave Pública (n, e): (" + str(n) + ", " + str(e) + ")")
print("Chave Privada (n, d): (" + str(n) + ", " + str(d) + ")")

tetas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'Ç', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â', 'Ê', 'Ô', 'À', ' ']

ASCII = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
         81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 128, 181, 144, 214, 224, 
         233, 199, 229, 182, 210, 226, 183, 32]

opcao = 0

while True:
    print("\n1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        texto = input('Digite o texto que deseja criptografar: ').upper()
        chaveN = int(input("Insira o valor de n da chave pública: "))
        chaveE = int(input("Insira o valor de e da chave pública: "))
        
        textoDiv = list(texto)
        textoCrip = []
        i = 0
        
        for caractere in textoDiv:
            while caractere != tetas[i]:
                i+=1
            textoCrip.append(ASCII[i])
            i = 0 
            
        for i in range(len(textoCrip)):
            textoCrip[i] = pow(textoCrip[i], chaveE) % chaveN
            print(str(textoCrip[i]), end=" ")
        print()
    
    elif opcao == '2':
        entrada = input('Digite os números criptografados (separados por espaço): ')
        chaveN = int(input("Insira o valor de n da chave privada: "))
        chaveD = int(input("Insira o valor de d da chave privada: "))
        
        textoCrip = [int(numero) for numero in entrada.split()]
        textoDescrip = []
        
        for i in range(len(textoCrip)):
            textoDescrip.append(pow(textoCrip[i], chaveD) % chaveN)
            
            j = 0
            while textoDescrip[i] != ASCII[j]:
                j += 1
            textoDescrip[i] = tetas[j]

            print(str(textoDescrip[i]), end="") 
        print()
    
    elif opcao == '3':
        print("Saindo...")
        break
        
    else:
        print("Opção inválida, tente novamente.")

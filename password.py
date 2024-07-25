import random
import string

opcao_de_senha = int(input("Digite '0' para criar sua propria senha ou '1' para usar uma aleatoria sugerida pelo programa: "))

if opcao_de_senha == 1:
    lowercase_letters = string.ascii_lowercase  
    uppercase_letters = string.ascii_uppercase 
    digits = string.digits  
    punctuation = string.punctuation 

    tamanho_da_senha = 10

    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    random_senha =  ''.join(random.choice(all_characters) for _ in range(tamanho_da_senha))

    print(f"Senha sugerida: {random_senha}")
else:
    contador = 1
    while (contador <= 5):
        senha = input("Crie sua senha: ")
        tamanho = len(senha)
        lower_senha = senha.lower()
        if(tamanho >= 10):
            if(lower_senha != senha):
                print("Senha valida. ")
                contador = 0
                while(contador != 5):
                    senha_confirmada = input("Confirme sua senha: ")
                    if(senha_confirmada == senha):
                        print("Senha confirmada!!")
                        break
                    else:
                        print("Senha incorreta.")
                        contador = contador + 1
                break
            else:
                if(contador == 5):
                    print("Voce atingiu o limite maximo de tentativas.")
                    break
                else:
                     print("Senha invalida. Digite uma senha com pelo menos 1 letra maiuscula. ")
                     contador = contador + 1
        
        else:
            if(contador == 5):
                print("Voce atingiu o limite maximo de tentativas")
                break
            else:
                print("Senha inválida. Digite uma senha com 10 ou mais caracteres. ")
                contador = contador + 1


    
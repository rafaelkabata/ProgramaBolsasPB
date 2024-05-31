import hashlib

def calcular_hash_sha1(string):
    # Converte a string em bytes (necessário para o hashlib)
    string_bytes = string.encode('utf-8')
    
    # Cria um objeto hash SHA-1
    hash_obj = hashlib.sha1()
    
    # Atualiza o hash com os bytes da string
    hash_obj.update(string_bytes)
    
    # Obtém o hash digest em formato hexadecimal
    hash_hex = hash_obj.hexdigest()
    
    return hash_hex

if __name__ == '__main__':
    while True:
        # Solicita uma string ao usuário
        entrada = input("Digite uma string (ou 'sair' para encerrar): ")
        
        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break
        
        # Calcula o hash SHA-1 da string fornecida
        hash_resultado = calcular_hash_sha1(entrada)
        
        # Imprime o hash resultante
        print("O hash SHA-1 da string é:", hash_resultado)
        print()  # Adiciona uma linha em branco para separar as saídas

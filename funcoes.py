import binascii
def xor(x, y):
    ans = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":
            ans += "1"
        else:
            ans += "0"
    return ans

def convert2Bin(chave, texto):
    if len(chave) == 8:
        return " ".join(f"{ord(i):08b}" for i in texto)
    if len(chave) == 16:
        return " ".join(f"{ord(i):08b}" for i in texto)

def criptografar(chave, chaveBinaria, arquivoBinario):
    
    #separando o arquivo em blocos do tamanho da chave
    if len(chave) == 8:
        
        if(len(arquivoBinario) % len(chaveBinaria) != 0):
            arquivoBinario += ' 00000000'
    elif len(chave) == 16:
        if(len(arquivoBinario) % len(chaveBinaria) != 0):
            arquivoBinario += ' 0000000000000000'
    
    
    chaveBinaria = chaveBinaria.replace(" ", "")
    arquivoBinario = arquivoBinario.replace(" ", "")

    print(chaveBinaria)
    print(arquivoBinario)

    #efetuando operação XOR entre chave e arquivo
    resultado = ''
    resultado += xor(arquivoBinario, chaveBinaria)
    print(resultado)
    return resultado

def decriptografar(chave, arquivo, chaveBinaria):
    chaveBinaria = chaveBinaria.replace(" ", "")

    print(chaveBinaria)
    print(arquivo)

    print(xor(arquivo, chaveBinaria))

    #efetuando operação XOR entre chave e arquivo
    aux = ''
    aux += xor(arquivo, chaveBinaria)

    resultado = '' 

    print(aux[0 : 0+8])
    print(int(aux[0 : 0+8], 2))
    print(aux[0 : 0+8])
    for i in range(0, len(aux), 8):
        resultado += chr(int(aux[i : i+8], 2))

    print(resultado)
    return resultado
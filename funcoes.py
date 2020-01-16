def xor(x, y):
    ans = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":
            ans += "1"
        else:
            ans += "0"
    return ans

def convert2Bin(texto):
    return " ".join(f"{ord(i):08b}" for i in texto)

def criptografar(chave, chaveBinaria, arquivoBinario):

    #garatindo que arquivo possa ser separado em partes iguais
    chaveBinaria = chaveBinaria.replace(" ", "")
    arquivoBinario = arquivoBinario.replace(" ", "")
    if len(chave) == 8 and len(arquivoBinario) % len(chaveBinaria) != 0:
        arquivoBinario += '00000000'
    elif len(chave) == 16 and len(arquivoBinario) % len(chaveBinaria) != 0:
        arquivoBinario += '0000000000000000'

    #separando o arquivo em blocos do tamanho da chave
    listaArquivoBinario = []
    for i in range(0, len(arquivoBinario), len(chaveBinaria)):
        listaArquivoBinario.append(arquivoBinario[i : i+len(chaveBinaria)])

    #efetuando operação XOR entre chave e arquivo
    resultado = ''
    for i in range(len(listaArquivoBinario)):
        resultado += xor(listaArquivoBinario[i], chaveBinaria)
    return resultado

def decriptografar(arquivo, chaveBinaria):
    
    #tirando espaços da chave
    chaveBinaria = chaveBinaria.replace(" ", "")

    #separando o arquivo em blocos do tamanho da chave
    listaArquivoBinario = []
    for i in range(0, len(arquivo), len(chaveBinaria)):
        listaArquivoBinario.append(arquivo[i : i+len(chaveBinaria)])

    #efetuando operação XOR entre chave e arquivo
    aux = ''
    for i in range(len(listaArquivoBinario)):
        aux += xor(listaArquivoBinario[i], chaveBinaria)

    #convertendo binário para string
    resultado = '' 
    for i in range(0, len(aux), 8):
        resultado += chr(int(aux[i : i+8], 2))
    return resultado
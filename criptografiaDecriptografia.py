import funcoes

#recebendo chave e endereço do arquivo a ser (de)criptografado
chave = "samuelsamuelsamu"
path = "arquivo.txt"
arquivo = open(path, 'r').read()

#transformando chave e arquivo em seus equivalentes binários
chaveBinaria = funcoes.convert2Bin(chave, chave)
arquivoBinario = funcoes.convert2Bin(chave, arquivo)

escolha = 'd'
if escolha == 'c' or escolha == 'C':

    #criptografando arquivo
    resultado = funcoes.criptografar(chave, chaveBinaria, arquivoBinario)

elif escolha == 'd' or escolha == 'D':
    
    #decriptografando arquivo
    resultado = funcoes.decriptografar(chave, arquivo, chaveBinaria)

#escrevendo resultado em arquivo
arquivoResultado = open('resultado.txt', 'w+')
arquivoResultado.write(resultado)
arquivoResultado.close()
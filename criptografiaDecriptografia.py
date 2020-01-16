import funcoes

#recebendo chave e endereço do arquivo a ser (de)criptografado
chave = input("Digite a chave de (de)criptografia:")
path = input("Digite o endereço do arquivo a ser (de)criptografado:")
arquivo = open(path, 'r').read()

#transformando chave e arquivo em seus equivalentes binários
chaveBinaria = funcoes.convert2Bin(chave)
arquivoBinario = funcoes.convert2Bin(arquivo)

escolha = input("Criptografar - C || Decriptografar - D:")
if escolha == 'c' or escolha == 'C':

    #criptografando arquivo
    resultado = funcoes.criptografar(chave, chaveBinaria, arquivoBinario)

elif escolha == 'd' or escolha == 'D':
    
    #decriptografando arquivo
    resultado = funcoes.decriptografar(arquivo, chaveBinaria)

#escrevendo resultado em arquivo
arquivoResultado = open('resultado.txt', 'w+')
arquivoResultado.write(resultado)
arquivoResultado.close()
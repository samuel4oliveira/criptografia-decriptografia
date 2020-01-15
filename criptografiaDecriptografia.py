import string
import funcoes
chave = "sa"
path = "arquivo.txt"
arquivo = open(path, 'r').read()
chaveBinaria = " ".join(f"{ord(i):08b}" for i in chave)
arquivoBinario = " ".join(f"{ord(i):08b}" for i in arquivo)

if(len(arquivoBinario) % len(chaveBinaria) != 0):
    arquivoBinario += ' 00000000'

listaArquivoBinario = arquivoBinario.split()

resultado = ''
for i in range(0, len(listaArquivoBinario), 2):
    resultado += funcoes.xor(listaArquivoBinario[0], listaArquivoBinario[1])
print(resultado)
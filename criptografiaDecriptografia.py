import binascii
chave = "samuello"
path = "arquivo.txt"
arquivo = open(path, 'r').read()
escolha = 'c'

while(len(arquivo) % len(chave) != 0):
    arquivo += '0'

# arquivoBinario = [bin(ord(x))[2:]for x in arquivo]
# chaveBinaria = [bin(ord(x))[2:]for x in chave]

print(arquivo)
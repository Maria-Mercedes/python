# função builtin Input, Print

# Função Input
# é sempre retornado como String

nome = input("Informe o seu nome:")
sobrenome = input("Informe o seu sobrenome:")

#Função Print
print(nome, sobrenome)
print(type(nome)) #printa o tipo da variável

print(nome, sobrenome, end="!\n") # parâmetro para adicionar algo ao final
print(nome, sobrenome, sep="-") # parâmetro para substituir um espaço por um caracter 
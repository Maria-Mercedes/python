saldo = 1000
saque = 200
limite = 100

# operador E -> para ser True, tudo tem que ser True
saldo >= saque and saque <= limite

# operador OU -> para ser True apenas um tem que ser True
saldo >= saque or saque <= limite

# operador Negação
not 1000 > 1500

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
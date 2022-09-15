print()
print(" _  _ ___   ___              _ _       ")
print("| || |__ \ / _ \            (_) |      ")
print("| || |_ ) | | | | __ ___   ___| | __ _ ")
print("|__   _/ /| | | |/ _` \ \ / / | |/ _` |")
print("   | |/ /_| |_| | (_| |\ V /| | | (_| |")
print("   |_|____|\___/ \__,_| \_/ |_|_|\__,_|")
print()
print() 

n=int (input("Introduce el numero de renglones del triangulo: "))
for i in range(n+1):
    print('*'*i)

for i in range(n+1):
    espacios=n-i
    print(' '*espacios+'*'*i)

for i in range(n+1):
    espacios=n-i
    print(' '*espacios+'* '*i)
# Questão 5

string = input("Digite algo: ")

string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("String original:", string)
print("String invertida:", string_invertida)

def inverterString(s):
    inverso = ""
    for char in s:
        inverso = char + inverso
    return inverso

string = input("Informe uma string para invertê-la: ")
resultado = inverterString(string)
print("String invertida:", resultado)
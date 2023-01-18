# Functia asta aduna 2 numere      
def add(x, y):
    return x + y

# Functia asta scade 2 numere
def subtract(x, y):
    return x - y

# Functia asta inmulteste 2 numere
def multiply(x, y):
    return x * y

# Functia asta imparte 2 numere
def divide(x, y):
    return x / y


print("Selecteaza operatia .")
print("1.Aduna")
print("2.Scade")
print("3.Inmulteste")
print("4.Imparte")

while True:
    # preia raspunsu de la user
    choice = input("Introdu alegerea(1/2/3/4): ")

    # verifica daca alegerea este una din cele 4 optiuni
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Introdu primul numar: "))
            num2 = float(input("Introdu al doilea numar: "))
        except ValueError:
            print("Valoare invalida. Te rog introdu un numar.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # verifica daca user-ul vrea alt calcul
        # rupe while loop daca raspunsul este nu
        next_calculation = input("Facem inca un calcul? (Da/Nu): ")
        if next_calculation == "Nu":
          break
    else:
        print("Valoare invalida")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1.Add  2.Sub  3.Mul  4.Div")
choice = input("Choose operation: ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    print("Result:", a / b)
else:
    print("Invalid choice")

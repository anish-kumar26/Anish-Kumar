while True:
    print("Welcome to math helper")
    print("What do you want to do: add, subtract, or multiply?")
    ans = input()

    if ans == "add": 
        print("Enter the first number to add")
        ans2 = float(input())
        print("Enter the second number you want to add")
        ans3 = float(input())
        result = ans2 + ans3
        print("Your answer is", result)
        break
    elif ans == "multiply":
        print("Enter first number you want to multiply")
        mul1 = float(input())
        print("Enter the second you want" )
    else:
        print("Invalid choice. Please choose 'add', 'subtract', or 'divide'. Try again.")

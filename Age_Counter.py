try:
    u = int(input("Enter an age :"))
    while u % 2 == 0:
        print("Ok, thank you!")
except ValueError:
    print("DO AS YOU ARE TOLD!")
except NameError:
    print("LEARN THE RULES FASTER!")
try:
    num1, num2 = eval(input("Enter two numbers separated by a comma :"))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error")
except SyntaxError:
    print("Comma is missing. Print 2 numbers like this - 1,2")
except:
    print("WRONG INPUT!!!")
else:
    print("NO EXCEPTIONS")
finally:
    print("This code will execute no matter what.")
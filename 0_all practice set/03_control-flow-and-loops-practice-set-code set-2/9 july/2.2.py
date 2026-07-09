num = int(input("enter any number for value 1 :"))
num2 = int(input("enter any number for value 2 :"))

# + - * /

operation = input("enter which operation you want to do with these 2 numbers + , - , * ,/")

match operation :
    case "+" :
        print(num + num2)
    case "-" :
        print(num - num2)
    case "*" :
        print(num * num2)
    case "/" :
        print(num / num2)

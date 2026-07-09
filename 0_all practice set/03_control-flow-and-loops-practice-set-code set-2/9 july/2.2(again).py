numberone = int(input("enter value for number 1 :"))
numbertwo = int(input("enter value for number 2 :"))

operation = input("enter what do you want to do with these numbers like + , - , * or / :")

match operation :
    case "+" :
        print(numberone + numbertwo)
    case "-" :
        print(numberone - numbertwo)
    case "*" :
        print(numberone * numbertwo)
    case "/" :
        print(numberone / numbertwo)
day = int(input("enter a day like 1 to 7 i will tell u whats the name of that day :"))

match day:
    case 1 :
        print("sunday")
    case 2 :
        print("monday")
    case 3 :
        print("tuseday")
    case 4 :
        print("wednesday")
    case 5 :
        print("thrusday")
    case 6 :
        print("friday")
    case 7 :
        print("satarday")
    case _ if day > 7 :
        print("there are only 7 days in a week")
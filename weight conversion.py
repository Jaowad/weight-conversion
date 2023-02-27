weight = int(input("what's your weight? "))
unit = input("In (K)g? / (L)b? ")

if unit == "l" or unit =="L":
    weight = weight * 0.454
    print("You weigth " + str(weight) + " kgs")
    if weight > 90:
        print("Loose some weight")
    elif weight < 50:
        print("Gain some weight")
    else:
        print("You are in good shape")
elif unit =="k" or unit =="K":
    weight = weight * 2.204
    print("You Weight " + str(weight) + " pounds")
    if weight > 198:
        print("Loose some weight")
    elif weight < 100:
        print("Gain some weight")
    else:
        print("You are in good shape")
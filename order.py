import random
def placeorder(drinktype, size, FCNo):
    random_number = random.randint(10000, 99999)
    order={}
    order['orderno']=str(random_number)
    order['drinktype']=str(drinktype)
    order['drinksize']=str(size)
    order['FCNo']=str(FCNo)
    print(str(order['orderno']))
    if ((random_number % 7) == 0 ):
        order['status']="No stock available"
    else:
        order['status']="Available"

    return order

def pricecalc(drinktype, size, FCNo):
    print("Here I am with drink " + str(drinktype) + " and size " + str(size))
    if (drinktype == "Pike Place Roast"):
        output= 3.75
    elif(drinktype == "Green Tea Latte"):
        output= 4.25
    elif(drinktype == "Caffe Latte"):
        output= 4.75
    else:
        output=6.25

    if (size == "Large"):
        output=output*1
    elif(size == "Grande"):
        output=output * 1.25
    else:
        output=output*1.5

    output=round(output,2)
    return(str(output))
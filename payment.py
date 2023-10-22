import random
def processpay(card, order):
    random_number = random.randint(100000, 450000)
    confirmn="Payment confirmation " + str(random_number) +": successful for order " + str(order) + " with card " + str(card)
    return confirmn

class OutofIngredientsError(Exception) :
    pass


def make_chai(milk , sugar ) :
    if milk == 0 or sugar == 0 :
        raise OutofIngredientsError("Missing milk or sugar")
    print("chai is ready...")



make_chai(0 ,1)
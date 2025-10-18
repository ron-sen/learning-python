class InavlidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"nasala": 20 , "ginger": 40}
    try:
        if flavor not in menu:
            raise InavlidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor]
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e :
        print("Error:" , e)
    finally :
        print("Thank you for visiting chaicode!")


bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)


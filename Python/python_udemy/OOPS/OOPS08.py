class BaseChai:
    def __inint__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger , cloves.")

class ChaiShope:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShope):
    chai_cls = MasalaChai

shop = ChaiShope()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()                                    
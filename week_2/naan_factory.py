class NaanFactory:
    def make_dough(self, item1, item2):
        if item1 == "water" and item2 == "flour":
            return "dough"
        return "not naan"
    
    def bake_dough(self, item):
        if item == "dough":
            return "naan"
        return "not naan"

    def run_factory(self, item1, item2):
        return self.bake_dough(self.make_dough(item1, item2))
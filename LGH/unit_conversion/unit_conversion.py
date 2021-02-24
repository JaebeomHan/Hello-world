class unit_conversion():

    def __init__(self, energy):
        self.energy = energy

    def to_hartree(self):
        return self.energy

    def to_J(self):
        return self.energy * (4.3597 * 10 - 18)

    def to_ev(self):
        return self.energy * 27.2114

    def to_kJmol(self):
        return self.energy * 2625

    def to_Kcalmol(self):
        return self.energy * 627.5

energy = 20
gg = unit_conversion(energy)
print("dh", gg.to_J())

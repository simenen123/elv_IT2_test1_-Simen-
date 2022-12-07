class frukt():
  def __init__(self, antall, noe_pris):
    self.antall = antall
    self.noe_pris = noe_pris

class kg_pris(frukt):
    def __init__(self, antall, noe_pris, rodhet):
        super().__init__(antall, noe_pris)
        self.rodhet = rodhet

    def pris(self):
        return self.antall * self.noe_pris * self.rodhet

eple = kg_pris(5, 5, 5)

print(eple.pris())
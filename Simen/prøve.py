class frukt():
  def __init__(self, antall, noe_pris):
    self.antall = antall
    self.noe_pris = noe_pris


# class pris_per_kilo(frukt):
#   def __init__(self, antall_kg, kg_pris):
#     super().__init__(antall_kg, kg_pris)
  
  
def regn_ut_pris(self):
  return self.antall * self.noe_pris

def select_vare():
    hvilken_vare = input("hvilken vare vil du ha? [epler] [appelsiner] [ananas]")
    if hvilken_vare == "epler":
      antall_kilo = input("hvor mange kilo vil du ha? (skriv bare tallet) ")
      eple = frukt(antall_kilo, 25)
      print(regn_ut_pris(eple))

# class pris_per_frukt(frukt):
#   def __init__(self, antall_frukt, pr_pris):
#     super().__init__(antall_frukt, pr_pris)


select_vare()

#   def beregnPris(self):
#       sluttpris = self.pris * self.rabatt
#       return rabattpris + (rabattpris * self.mva)

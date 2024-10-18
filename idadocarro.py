carro = int(input("Idade do carro:"))

import datetime
hoje = datetime.date.today()
anodoje = hoje.year

if carro <= anodoje - 1886:
   if carro <= 10:
       print("Seu carro é seminovo.")
   else:
       print("Seu carro é antigo.")
else:
    print("seu carro tá velho demais para ser carro também como é possível ter um carro desse")



























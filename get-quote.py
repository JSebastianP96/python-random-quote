import random
def principal():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  star = 0
  last = len(quotes)-1
  for i in range(0,3,1): #Ciclo for para generar multiple cotizaciónes
    rnd = random.randint(star,last)#seleccio aleatoria de posicion de la matriz
    print(quotes[rnd])

if __name__== "__main__":
  principal()

import random
def principal():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  star = 0
  last = len(quotes)-1
  rnd = random.randint(star,last)
  print(rnd)
  print(quotes[rnd])

if __name__== "__main__":
  principal()

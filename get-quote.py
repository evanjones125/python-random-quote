import random

f = open("quotes.txt")
quotes = f.readlines()
last = len(quotes) - 1
rnd = random.randint(0, last)

def main():

  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  main()

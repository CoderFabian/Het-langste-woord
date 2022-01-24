import random
doorgaan = True
aantal_goed = 0

woorden = ["boom", "school", "pen"]

naam = str(input("Wat is jouw naam?: "))
print("Welkom" , naam,"maak een woord met de volgende letters: ")

while doorgaan:
  x = woorden[random.randint(0,2)]
  shuffled = list(x)
  random.shuffle(shuffled)
  shuffled = ' '.join(shuffled)
  print(shuffled)
  shuffle_vraag = input("Welke woord denk je dat er staat?: ")
  if shuffle_vraag == "stop":
    doorgaan = False
    print("Wij zijn gestopt jij had" ,aantal_goed, "vragen goed!")
    break
  if shuffle_vraag == x:
    print("Goed!")
    aantal_goed = aantal_goed+1
  else:
    print("fout...")
  if aantal_goed == 1:
    print("Je hebt nog maar" ,aantal_goed, "vraag goed!")
  else:
    print("Je hebt" ,aantal_goed, "vragen goed!")
  print("type 'stop' om te stoppen")
x = True
def Check_Age():
  gj = int(input("Uit welk jaar komt u? : "))
  if 2023-gj >= 18:
    print("Gefeliciteerd je bent oud genoeg")
  else:
    print("Sorry, je bent niet oud genoeg")

while x == True:
  Check_Age()
  y = input("Stoppen? y/n ")
  if y =="y":
    x = False
else:
  print("Bye Bye!")

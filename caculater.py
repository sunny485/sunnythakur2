cyan = "\033[1;36m"
print(cyan+'           this calculater is created by sunny thakur')
def sunny():
 blue = "\033[1;34m"
 cyan = "\033[1;36m"
 red = "\033[1;31m"
 b1 = float(input(blue+"enter number: "))
 op = (input(blue+"enter opreter: "))
 n2 = float(input(blue+"enter second number: "))
 if op == "+":
     print(b1 + n2)
 elif op == "-":
     print(b1 - n2)
 elif op == "/":
     print(b1 / n2)
 elif op == "*":
    print(b1 * n2)
 else:
    print("invailed oprater")
while True:
  blue = "\033[1;34m"
  red = "\033[1;31m"
  d=input(blue+' to calculate enter y to exit enter n ')
  if d == "y":
    sunny()
    continue
  else:
    print(red+'thank you for using')
    break
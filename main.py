#Write your code below this line 👇
import math
def prime_checker(number):
  # half = round(number/2)
  root = round(math.sqrt(number))
  # for i in range(2, half + 1):
  # print(f"Checking number {number}")
  for i in range(2, root + 1):  
    # print(f"dividing by {i} -- quotient = {number%i} ")    
    if number%i == 0:
      return False # not a prime number
  return True #default - it's prime



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
debugnumbers = []
n = int(input("Check this number: "))
debugnumbers.append(n)
# debugnumbers = [10, 25, 31, 67, 73]
# for n in range(0, 120):
for n in debugnumbers:
  prime = prime_checker(number=n)
  if prime:
    print(f"It's a prime number.")
  else:
    print("It's not a prime number.")
    # print(f"               {n} is not prime")
#Write your code below this line 👇

def prime_checker(number):
  half = round(number/2)
  for i in range(2, half + 1):
    if number%i == 0:
      return False
  return True #default - it's prime



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
for n in range(0, 101):
  prime = prime_checker(number=n)
  if prime:
    print(f"{n} is prime")
  else:
    print(f"               {n} is not prime")
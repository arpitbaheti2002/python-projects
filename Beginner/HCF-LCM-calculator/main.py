import math

def find_hcf(x, y):
    '''Returns the hcf of two numbers'''
    while(y):
        temp = y
        y = x % y
        x =temp
    return x

def find_lcm(x, y):
    '''Returns the lcm of two numbers'''
    return (x*y)/find_hcf(x,y)

query = input("Enter your query: ")
method = None
num = []

if "HCF".lower() in query.lower() and "LCM".lower() in query.lower():
    print("You can only perform either HCF or LCM at a time.")

elif "HCF".lower() in query.lower():
    method = "HCF"
elif "LCM".lower() in query.lower():
    method = "LCM"

words = query.split(' ')

for word in words:
    temp_words = word.split(',')
    for _ in temp_words:
        if _.isdigit():
            num.append(int(_))
        

if method==None or not num:
    print("Query was not understood. Please try again!")

else:
  res = num[0]
  for n in num[1:]:
      if method=='HCF':
          res = find_hcf(res, n)
      
      else:
          res = find_lcm(res, n)

  print(f"\n\nThe result is {res}.")
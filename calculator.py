def add(a,b):
   return a+b

def subtract(a,b):
   return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
   if (b == 0):
        return "cannot divide by zero"
   return a/b


print("addition:", add(10,5))
print("subtract:", subtract(10,5))
print("multiplication:", multiply(10,5))
print("division:",divide(10,5))

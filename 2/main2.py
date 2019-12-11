def f(a):
  a.append(7)

def g(a):
  print(a)

a = [1, 2]

f(a)
print(a)
g(a)
print(a)
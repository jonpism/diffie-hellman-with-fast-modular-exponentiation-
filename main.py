# fast modular exponentiation function to return the result: base**exponent % modulus
def fme(b, m, e):
  result = 1
  while e > 0:
    if e % 2 == 1:
      result = (result * b) % m
    e //= 2
    b = (b ** 2) % m
  return result


b = int(input("Give base: "))
m = int(input("Give modulus: "))
expA = int(input("Give exponent a: "))
expB = int(input("Give exponent b: "))

A = fme(b, m, expA)
B = fme(b, m, expB)
print("Alice=", b, "^", expA, "mod", m, "= Α=", A)
print("Bob=", b, "^", expB, "mod", m, "= B=", B)

print("Alice calculates: ", end='')
print("B ^", expA, "mod", m, "=", fme(B, m, expA))
print("Bob calculates: ", end='')
print("A ^", expB, "mod", m, "=", fme(A, m, expB))

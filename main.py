#Shane Edwards
#Constructing a Logical Circuit 


def half_Adder(i,j):

  sum = i ^ j  # Compute the sum bit using the XOR (^) operation
  carry = i & j # Compute the carry bit using the AND (&) operation

  return(sum,carry) # Return a tuple containing the sum and carry bits

print("Half-Adder")
# Iterate through all possible combinations of input values 0 and 1 for i and j
for i in [0, 1]: 
  for j in [0, 1]:
    sum, carry = half_Adder(i, j)
    print("i = {}\tj = {} | c = {}\ts = {}".format(i, j, carry, sum))


# Define a function called full_Adder that takes three binary digits i, j, and k as input
def full_Adder(i, j, k):
  sum, carry1 = half_Adder(i, j) #compute sum and carry for first two bits 
  sum, carry2 = half_Adder(sum, k) #compute final sum and carry including thrid bit
  carry = carry1 | carry2 #combine carries using or to get final
  return(sum, carry) #Return tuple

print("Full-Adder")
# Iterate through all possible combinations of input values 0 and 1 for i, j, and k
for i in [0, 1]:
  for j in [0, 1]:
    for k in [0, 1]:
      sum, carry = full_Adder(i, j, k)
      print("i = {}\tj = {}\tk = {} | c = {}\ts = {}".format(i, j, k, carry, sum))

# Define a function that takes six binary digits (a, b, c, d, e, f) as input
def parallel_Adder(a, b, c, d, e, f):
  sum1, carry1 = full_Adder(a, d, 0) #no initial carry so use 0
  sum2, carry2 = full_Adder(b, e, carry1)
  sum3, carry3 = full_Adder(c, f, carry2)
  return(sum1, sum2, sum3, carry3) #three sums and final carry

#binary inputs from the example 
a = 0
b = 1
c = 1
d = 1
e = 1
f = 0

w, x, y, z = parallel_Adder(a, b, c, d, e, f)
print("{}{}{} + {}{}{} = {}{}{}{}".format(a, b, c, d, e, f, w, x, y, z)) #print input/result
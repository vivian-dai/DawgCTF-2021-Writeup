from pwn import * # Import pwn library

# METHODS 

# Returns whether n is a perfect square
def isPerfectSquare(n):
    m = int(math.sqrt(n))
    return m*m == n

# Returns true if n is a Fibinacci number, else false
def isFibonacci(n):
    # n is a Fibonacci number if one of 5*n*n + 4 or 5*n*n - 4 is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# Computes which number is a Fibonacci number and returns it
def compute():
    s = c.recvline()
    s = s.decode("utf-8")
    s = s[1:-2]
    s = s.split(", ")
    print(s)
    lst = []
    for i in s:
        lst.append(int(i))
    print(lst)
    for i in lst:
        if isFibonacci(i):
            c.sendline(encode(str(i)))
            print(i)
    print(c.recvline())
    print(c.recvline())

c = remote("umbccd.io", 6000)
for i in range(10):
    print(c.recvline())
for i in range(100):
    compute()
print(c.recvline())

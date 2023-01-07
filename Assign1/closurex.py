# closure implementation
# closure is a nested function that can access outer  funtion's variable even if that function is closed

def add_n(n):
    def addition(x):
        return x+n
    return addition

add_5 = add_n(5)  #calling outer function that will hold one operand
add_10 = add_n(10)

print(add_5(4))  #return sum of n and number passed
print(add_10(4))
print(add_10(add_5(4)))

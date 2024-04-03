def fact(n): 
    if n == 1: 
        return 1 
    else: 
        return n-1 + fact(n-1)
print(fact(10))


# def cars(p, y):
#     if y == 0:
#         return p
#     else:
#         for _ in range(y):
#             p -= 1/5 * p  
#         return p 
# result = cars(12000, 3)
# print((round(result, 2)))
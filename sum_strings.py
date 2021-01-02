"""Sum two strings together and return a string."""


def sum_str(a, b):
    """Sum two numbers and return a string."""
    a = str(a)
    b = str(b)
    if a.isnumeric() and b == "":
        b = 0
        results = str(int(a) + int(b))
    elif a == "" and b.isnumeric():
        a = 0
        results = str(int(a) + int(b))
    elif a.isnumeric() and b.isnumeric():
        results = str(int(a) + int(b))
    else:
        results = str(0)
    return results

results = sum_str("4", "5")
print(results)



# Other Solutions:
# 1. 
# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))

# 2.
# def sum_str(a, b):
#     print(a, b)
#     if a == "" or a == None: a = "0"
#     if b == "" or b == None: b = "0"
#     return str(int(a)+int(b))

# 3. 
# def sum_str(a, b):
#     # happy coding !
#     if a =='' and b=='':return'0'
#     if b =='':return a
#     if a =='':return b
#     if a =='' and b=='':return'0'
#     return str(int(a)+int(b))
#     pass
# 4. 
# def sum_str(a, b):
#     return '%d' % (int(a if a else 0) + int(b if b else 0))

# 5. 
# # Why stop at 2 arguments?
# def sum_str(*args):
#     return str(sum(map(int, filter(None, args))))

# 6. 
# def sum_str(*args):
#     return str(sum(map(lambda x:int(x) if x != '' else 0, args)))
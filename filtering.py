def func(x):
    variables = ["a","e","i","o","u"]
    
    if x in variables:
        return True
    else:
        return False
alphabet = ["a","b","c","d","e","u"]

results = filter(func, alphabet)
print(list(results))

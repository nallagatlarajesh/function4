def is_even(x):
    return x%2==0
nums=[2,5,7,9,3,4,6,8,9,2,4,56,67,7]
evens=list(filter(is_even,nums))

print(evens)

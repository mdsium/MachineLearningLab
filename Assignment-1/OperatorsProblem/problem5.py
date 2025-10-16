# Write a program to demonstrate the behavior of pre-increment and post-increment operators.

def pre_increment(x):
    x = x + 1
    print("Pre-Incremented Value:", x)
    return x

def post_increment(x):
    print("Post-Incremented Value (before increment):", x)
    x = x + 1
    return x

# Initial value
i = 5

print("Initial value of i:", i)

# Pre-increment simulation
i = pre_increment(i)  # should print 6

# Post-increment simulation
i = post_increment(i)  # should print 6 before increment, i becomes 7

print("Final value of i after both operations:", i)

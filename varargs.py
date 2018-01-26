# VARARGS
# Where I first learned about them http://book.pythontips.com/en/latest/args_and_kwargs.html
# What the link has to say about VarArgs    
#    " *args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. 
#     What variable means here is that you do not know beforehand how many arguments can be passed to your function by the user so in this case you use these two keywords. 
#     *args is used to send a non-keyworded variable length argument list to the function." 


# Below is code from his article that jumped out to me:
# --------------------------------------------------------------------------------------------------
# def test_args_kwargs(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)

# first with *args
# >>> args = ("two", 3, 5)
# >>> test_args_kwargs(*args)
# arg1: two
# arg2: 3
# arg3: 5

# now with **kwargs:
# >>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
# >>> test_args_kwargs(**kwargs)
# arg1: 5
# arg2: two
# arg3: 3
# --------------------------------------------------------------------------------------------------

# I thought to myself "He is teaching us how to use any variable amount of arguments. Why doesn't his test_atgs_kwags function take a variable ammount of arguments? Most likely due to ease of instruction, considering he is teaching us about these at the moment.
# Probably not the best idea to use a concept to teach how it works! However, it could be  
# So I refactored his code to be more general, like the following:

def test_args_kwargs(*args):
    for index, i in enumerate(args):
        print("arg" + str(index + 1) + ": " + str(i))

# For example, here's what would happen if I put the following into console.

# >>> test_args_kwargs('a')
# arg1: a

# >>> test_args_kwargs('a', 'b')
# arg1: a
# arg2: b

# --------------------------------------------------------------------------------------------------
# Try it out for yourself! Copy and paste the following line and remove or add any other characters or strings to it that you please.
# test_args_kwargs('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
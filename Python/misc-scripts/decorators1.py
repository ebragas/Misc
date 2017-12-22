# https://realpython.com/blog/python/primer-on-python-decorators/

# # First class objects
# def foo(bar):
#     return bar + 1

# # Returning functions
# def parent(num):
    
#     def first_child():
#         return "Printing from the first_child() function."

#     def second_child():
#         return "Printing from the second_child() function."

#     try:
#         assert num == 10
#         return first_child
#     except AssertionError:
#         return second_child

# foo = parent(10)
# bar = parent(11)

# print(foo)
# print(bar)

# print(foo())
# print(bar())


# # Example 1
# def my_decorator(some_function):
    
#     def wrapper():

#         print("Something is happening before some_function() is called")
#         some_function()
#         print("Something is happening after some_function() is called.")
    
#     return wrapper

# def just_some_function():
#     print("Wheee!")

# just_some_function()
# just_some_function = my_decorator(just_some_function)
# just_some_function()


# # Example 2
# def my_decorator(some_function):

#     def wrapper():
#         num = 10
#         if num == 10:
#             print("Yes!")
#         else:
#             print("No!")

#         some_function()

#         print("Something is happening after some_function() is called.")

#     return wrapper

# def just_some_function():
#     print("Wheee!")

# just_some_function()
# just_some_function = my_decorator(just_some_function)
# just_some_function()


# from decorator07 import my_decorator

# @my_decorator
# def just_some_function():
#     print("Wheee!")

# just_some_function()


# Real world example
import time

def timing_function(some_function):
    """
    Outputs the time a function takes to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: {}\n".format(t2 - t1)

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function())

import my_module
import random

print(my_module.pi)
#A module is basically used to split codes into different batches
#"my_module" is module created under the main module and it is imported
#pi is a variable created in the my_module module, it can be echoed here
#in the main file after being imported.

random_number = random.randint(1,10)
random_float = random.random()
multiple_float = random_float * 10
print(random_number)
print(random_float)
print(multiple_float)

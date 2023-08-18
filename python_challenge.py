"""
--Assignement--
Create and call a python function that : 
- stores a random integer A between 1 and 9
- stores a random integer B between 1 and 9
- multiplies A and B together as C
- Prints A and C for every result until C = 4
- If C = 4 , print ‘Success!’ and the results for A and B
- Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV
"""
from random import randint

def random_function():
    A = randint(1,9)
    B = randint(1,9)
    C = A*B

    i = 1
    while C != 4:
        print("-- Iter " + str(i) + " --")
        print("A = {a} C = {c}".format(a=A, c=C))

        A = randint(1,9)
        B = randint(1,9)
        C = A*B

        i+=1

    print("-- Iter " + str(i) + " --")
    print("Success!")
    print("A = {a} B = {c}".format(a=A, c=B))

random_function()

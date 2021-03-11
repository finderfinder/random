'''
Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''

for i in range(1,101):
    output = ""
    if i % 3 == 0:
        output = output + "Fizz"
    if i % 5 == 0:
        output = output + "Buzz"
    if output == "":
        output = str(i)
    print (output)

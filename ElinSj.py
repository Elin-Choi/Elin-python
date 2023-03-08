# variable=len("hello world")
# print(variable)
# print(variable[3])
# print("hello"+""+"world")
# variable="hello world"
# print(variable[-3])
# print(variable[1:4])
# print(variable[6:])

# variable="%d books" % 3
# print(variable)

# variable="%s books" % "3"
# print(variable)

# number=3
# # variable=f'I have {number+2} books'
# # print(variable)

# variable="I have %d apples and %d books" % (number, number+1)
# print(variable)

# variable="The error rates : %d%%" % 55
# print(variable)


# variable="%10s" % "hello"
# print(variable)
# variable="%-10s" % "hello"
# print(variable)

# variable="{0:>10}".format("hello")
# print(variable)

# variable="{0:^10}".format("hello")
# variable="{0:>10}".format("hello")
# print(variable)

# variable="{0:-^10}".format("hello")
# print(variable)

# variable=input()
# print("Input String %s, Ineger %d" % (variable, int(variable)))

# variable=input("enter a number")

# for variable in range(1,10):
#      print(variable, end="")

file=open("test.txt", "w")
for data in range(1, 11):
    file.write(f'{data} line\n');
file.close()

file=open("test.txt", "a")
for data in range(1, 11):
    file.write
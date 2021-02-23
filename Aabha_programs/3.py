#With a given integral number n, write a program to generate a dictionary
#that contains (i, i x i) such that is an integral number between 1 and n
#(both included). and then the program should print the dictionary.Suppose
#the following input is supplied to the program: 8

no=int(input('Enter a number:'))
dic=dict()
for x in range(1,no+1):
    dic[x]=x*x
print(dic)

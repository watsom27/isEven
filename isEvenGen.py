file = open("isEven.py", "w")
file.write("def isEven(nbr):\n    if(nbr == '0'): return False\n")

output = ""

for i in range(1,10000000):
    print(i)
    truefalse = (i%2==0)
    file.write("    if(nbr == '")
    file.write(str(i))
    file.write("'): return ")
    file.write(str(truefalse))
    file.write("\n")
    file.flush()

file.write(output)
file.write("\n\nnbr = input(\"Enter number:\")\nprint(isEven(nbr))")
file.close()

print("done")
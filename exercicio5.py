inp = input("Digite alguma coisa: ")
print("")
if(inp.isalpha()):
    print(inp + " é uma String!" '\n')

if(inp.isnumeric()):
    print(inp, " é uma int!" '\n')

if(inp.isalnum() and not(inp.isalpha()) and not(inp.isnumeric())):
    print(inp, " tem int e String!")
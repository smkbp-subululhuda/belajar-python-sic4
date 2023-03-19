input = [800,600,400,200]
compared = [500,200,400]

if len(input) != len(compared):
    compared.append(input[len(input)-1])
else:
    compared = compared

print(input)
print(compared)

for value in range(len(input)):
    if  input[value] == compared[value]:
        input[value] = 1
    else:
        input[value] = 0

print(input)
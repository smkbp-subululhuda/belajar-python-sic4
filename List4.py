# Masih Salah

input = [100,200,300,400,500]
compared = [500,200,400]

# hasil = [100,0,300,0,0]
if len(input) != len(compared):
    compared.append(input[len(input) - 2])
    compared.append(input[len(input) - 1])
else:
    compared = compared

# print(input)
# print(compared)

for value in range(len(input)):
    if  input[value] == compared[value]:
        input[value] = 1
    else:
        input[value] = 0
print(input)
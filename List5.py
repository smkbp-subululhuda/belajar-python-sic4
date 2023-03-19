# Challenge 1

input = [100, 200, 300, 400, 500]
compared_input = [500, 200, 400]

if len(input) != len(compared_input):
    compared_input.append(input[len(input) - 2])
    compared_input.append(input[len(input) - 1])
else:
    compared_input = compared_input

for value in range(len(input)):
    if input[value] == compared_input[value]:
        input[value] = 0
    else:
        input[value] = input[value]

print(input)
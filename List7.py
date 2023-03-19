# Challenge 2
# output = {
#     "highest_salary":"Dwi",
#     "total_salary":19000
# }

input = [
    {'nama':'Budi','gaji':5000},
    {'nama':'Dwi','gaji':8000},
    {'nama':'Joko','gaji':6000}
]

salary = []
for value in range(len(input)):
    # print(input[value]['gaji'])
    salary.append(input[value]['gaji'])

salary_tertinggi = max(salary)
# print(salary)
# print(salary_tertinggi)

nama_tertinggi = input[salary.index(salary_tertinggi)]['nama']
# print(nama_tertinggi)

total_salary = sum(salary)
# print(total_salary)

output = {
    "highest_salary":nama_tertinggi,
    "total_salary":total_salary
}
print(output)
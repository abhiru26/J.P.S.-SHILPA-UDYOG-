n = int(input())

numbers = input()

numbers = list(map(int, numbers.split()))

final_data = [1]
j = 1
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        j = j + 1
        final_data.append(j)
    else:
        final_data.append(1)

for item in final_data:
    print(item, end=" ")

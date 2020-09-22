n, k = list(map(int, input().split()))
data = list(map(str, input().split()))
#print(data)
#print(n, k)
#print(type(n))

count = 0
for i in range(len(data)-2):
    if (data[i] == 'P' and data[i + 1] == 'T') or (data[i] == 'T' and data[i + 1] == 'P'):
        count = count + 1
print(count)

card_no = []
#abhi = int(input().split())
#print(abhi)
a,b,c,d,e = input().split()

def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


l = [int(a),int(b),int(c),int(d),int(e)]

if int(a) or int(b) or int(c) or int(d) or int(e) > 10**6:
    print('Wrong Input')
    exit()
if int(a) or int(b) or int(c) or int(d) or int(e) <1:
    print('Wrong Input')
    exit()

num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])

print(gcd)


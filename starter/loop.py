sum  = 0
for x in range(101):
    sum = sum + x
print(sum)

# 类似于 JavaScript 中的 for...in... loop
L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print("Hello, %s" %name)
    print("Hello, " + name)
# break

n = 0
while n < 100:
    n = n + 1
    if n % 2:
        continue
    #print(n)
print('END')

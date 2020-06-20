import bisect
words = "Anacell provides the best services in the city"
word = "abcdefghijklmnopqrstuvwxyz"
idx = bisect.bisect_left(word, "km")
print("idx:", idx)


a = "bfcde"
idx = bisect.bisect_left(a, "f")
print("idx:", idx)
idx2 = bisect.bisect_left(a[:idx], "f")
print("idx2:", idx2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = set()
ta = tuple(a)
print("ta:", ta)
s.add(ta)
print("s:", s)

n = [0]
N = n[:0] + n[1:]
print("N:", N)

a = [1, [3, [4], [5]]]


str2 = "123 sjhid dhi"
list2 = str2.split()  # or list2 = str2.split(" ")
print list2


def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


print(power(5))

print("2**30:", 2**30)

print(1//2)

a = "abcdefg"
b = "hjklmn"
for (x, y) in zip(a, b):
    print("x,y:", (x, y))

c = "abc"
d = "abca"
print(c > d)
print(d > c)

str = "banana"
print("ana" in str)

str = "1"*10
print("str:", str)

a = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
for row in a:
    row = "".join(row)
    print("row:", row)
print("a:", a)

a = "1+4*2"
print(a[4:-2])
print(a[1:-2])
print(a[4:-2])


print(int(a))

pld = "abcdef"
print("pld:", pld[::-1])

a = ""
a += str(1)
print("a:", a)

for i in range(11, 1):
    print("i:", i)

words = "Anacell provides the best services in the city"
#words_split = words.split(" ")
#print("words_split:", words_split)
a = set(words)
print("a:", a)

words = "Anacell provides the best services in the city"
print("words", words.lower())

word = "Anacell"

words = "Anacell provides the best services in the city"
idx = bisect.bisect_left(" ")
print("idx:", idx)

for i in range(10)[::-1]:
    print("i:", i)


i = 10

for j in range(i+1, i+1):
    print("jk:", j)

print("j:", j)

strg = "a#b#c#d#e#f"
strg = strg.replace("#", "")
print("strg:", strg)

name = "Bob"
print(name.lower())

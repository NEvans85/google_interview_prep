# f = open("A-small-practice.in.txt", 'r')
# o = open("A-small-practice.out.txt", 'w')
f = open("A-large-practice.in.txt", 'r')
o = open("A-large-practice.old.txt", 'w')
n = int(f.readline())


def flipCake(status):
    if status == "-":
        return "+"
    else:
        return "-"
        
for case in range(n):
    s, k = f.readline().split(" ")
    k = int(k)
    count = 0
    s = list(s)
    l = len(s) - (k - 1)
    for idx in range(l):
        if s[idx] == "-":
            count += 1
            for kIdx in range(k):
                s[idx + kIdx] = flipCake(s[idx + kIdx])
    rest = s[l : ]
    if all([x == "+" for x in rest]):
        o.write("Case #" + str(case + 1) + ": " + str(count) + "\n")
    else:
        o.write("Case #" + str(case + 1) + ": IMPOSSIBLE\n")
o.close()
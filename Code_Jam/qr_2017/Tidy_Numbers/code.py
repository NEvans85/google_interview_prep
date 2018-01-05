# f = open("B-small-practice.in.txt", 'r')
# o = open("B-small-practice.out.txt", 'w')
f = open("B-large-practice.in.txt", 'r')
o = open("B-large-practice.old.txt", 'w')
n = int(f.readline())

# Naive solution: count backwards from the number, checking each for tidyness.

def isTidy(numStr):
    for idx in range(1, len(numStr)):
        if numStr[idx] < numStr[idx - 1]:
            return False
    return True
    
for case in range(n):
    i = int(f.readline())
    while not isTidy(str(i)):
        i -= 1
    o.write("Case #" + str(case + 1) + ": " + str(i) + "\n")
o.close()
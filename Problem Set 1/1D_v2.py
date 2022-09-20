# Read inputs: work

lines=[]
for i in range(int(input())):
    lines.append(input().split(" "))
print(lines)

# First conversion
int_result=0
n=0
adict = {lines[i][1][i]: i for i in range(len(lines[i][1]))}
for i in reversed(lines[i][0]):
    # Yet to understand
    # The Trick: 
    # result= dictionary(number assigned by char)* (length of the message itself^n)
    int_result += adict[i] * len(lines[i][1]) ** n
    # print(int_result)
    n += 1

alist = []
    # assign a character iteratively in numbers
adict = {i: lines[i][2][i] for i in range(len(lines[i][2]))}

    # reapplying those changes (still don't understand)
while int_result > 0:
    alist = [adict[int_result % len(lines[i][2])]] + alist
    print(alist)
    int_result //= len(lines[i][2])

# join the list elemetns into a string, return it
final="".join(alist)


for i in range(len(lines)):
    # print("Case #{0}: {1}".format(i+1, int_to_base(base_to_int(lines[i][0], lines[i][1]), lines[i][2])))
    print("Case #{0}: {1}".format(i+1,final))

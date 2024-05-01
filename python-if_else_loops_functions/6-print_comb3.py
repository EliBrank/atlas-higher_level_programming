#!/usr/bin/python3

first_num = True

for i in range(10):
    for j in range(10):
        if (i < j):
            if first_num is True:
                print("{}{}".format(str(i), str(j)), end='')
                first_num = False
            else:
                print(", {}{}".format(str(i), str(j)), end='')
print("")

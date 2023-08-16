# for inx in range(6):
#  for jnx in range(inx + 1):
#     print("*", end="")
#  print("@")

print('-------------------')

inx = 0
while inx < 6:
    jnx = 0
    while jnx < inx + 1:
        print("*", end="")
        jnx += 1
    print("@", end="")
    inx += 1
    print()

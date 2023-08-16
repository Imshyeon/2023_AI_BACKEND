
# for inx in range(6):
#     n=0
#     for jnx in range(inx + 1):
#         print("*", end="")
#         print("@")
#         n+=1
#     print(f'n:{n}')
#
inx = 0
while inx < 6:
    jnx = 0
    while jnx < inx+1:
        print("*@")
        jnx += 1
    inx += 1
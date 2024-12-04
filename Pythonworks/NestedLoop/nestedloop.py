# $

#$  $

#$  $   $

#$  $   $   $

#$  $   $   $   $

#$  $   $   $   $   $


# for row in range(1,7):

#     for col in range(1,row+1):

#         print("$",end="\t")

#     print()

#   1
#   2   2
#   3   3   3
#   4   4   4   4
#   5   5   5   5   5


# for row in range(1,6):

#     for col in range(1,row+1):

#         print(row,end="\t")

#     print()

#5  *    *   *   *   * col in range(1,6)
#4  *    *   *   * range(1,5)
#3  *    *   *range(1,4)
#2  *    *range(1,3)
#1 *  range(1,2)


for row in range(5,0,-1):

    for col in range(1,row+1):

        print("*",end="\t")

    print("")


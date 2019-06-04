import math;
a = 1
b = 30
# print('1')

array = [1,2,3,4,5]

# hi = input("whats your name")

# print(int(math.pow(3,2)))

# if a > 10:
#     print("yupp")
# elif a > 5:
#     print(" elif worked")
# else:
#     print('elsee workedd'):

# print(5//2)


## Pyramid building
# for element in range(1,6):
#     for value in range(6 - element):
#         print(" ", end="")
#     for start in range(element):
#         print("* ", end="")
#     for value in range(6 - element):
#         print(" ", end="")
#     print()

#
# num = int(input("Enter a number?:  "))
# flag = 0
#
# ### Prints all primes in a given range
#
# for value in range(2, num):
#     flag = 0
#     for element in range(2, value):
#         if value%element == 0:
#             flag = 1
#             break
#     if flag ==1:
#         print("not a prime")
#     else:
#         print("PRIME= ", value)

# findNum = int(input("enter a number:  "))
#
# array1 = [2,4,7,8]
#
# for x in array1:
#     if array1[x]== findNum :
#         print(x)
#         break


a = [1,2,3,4,5,6,7,8,9,10,11,12,13]

findNum = int(input("Enter a Number: "))

answer = 0


beg = 0
end = len(a)-1

test = a[0] + a[5]



while beg<=end:
    mid= int((beg+end//2))
    if findNum == a[mid]:
        answer = 1
        break
    elif findNum > int(a[mid]):
        beg = mid+1
    else:
        end = mid-1
if answer == 1:
    print("element found at index", mid)
    print("element = ", a[mid])




#





    #

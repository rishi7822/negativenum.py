list1 = [23,-34,-22,45,66]

neg_nos = [num for num in list1 if num < 0]

print("negative numbers are:", *neg_nos)

#RANGE FUNTION

start = int(input("enter the first:"))
end = int(input("enter the second number:"))

for i in range(start , end+1):

    #condition
    if i < 0:
        print(i, end = " ")
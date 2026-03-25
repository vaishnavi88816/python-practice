list=[2,37,9,34,65,56]
largest=list[0]
index=0
for i in range(len(list)):
    if list[i]>largest:
        largest=list[i]
        index=i
print(f"your largest number is {largest} at index {index}")
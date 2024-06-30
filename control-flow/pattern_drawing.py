size=int(input("Enter the size of the pattern:"))
i=size
while size>0:

    for i in range(1,i+1):
        print("*", end="")
    print()
    size-=1

def swapFileData():
    fileToOpen1 = input("Enter the first file name with extension that you want to swap: ")
    with open(fileToOpen1, 'r') as a:
        data_a = a.read()

    fileToOpen2 = input("Enter the second file name with extension that you want to swap: ")
    with open(fileToOpen2, 'r') as b:
        data_b = b.read()

    with open(fileToOpen1, "w") as a:
        a.write(data_b)

    with open(fileToOpen2, "w") as b:
        b.write(data_a)

    #data_a = open(fileToOpen1, 'r')
    #data_b = open(fileToOpen2, 'r')
    
    print(data_b)
    print(data_a)

swapFileData()
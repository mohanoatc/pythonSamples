for bottles in range(10, 0, -1):
    if bottles > 1:
        print(bottles, " bottles of beer on the wall")
        print(bottles, " bottles of the beer ")
    else:
        print(bottles, " bottle of beer on the wall")
        print(bottles, " bottle of the beer ")
    print("Take one down.\nPass it around.")
    if bottles > 1:
        print(bottles - 1, "bottle of beer on the wall\n")
    else:
        print("No more bottles of beer on the wall\n")


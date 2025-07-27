def common_elements():
    set3 = set(range(0,100,3))
    set5 = set(range(0,100,5))
    print("set3: ", set3)
    print("set5: ", set5)
    return set3 & set5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("ОК")
def proc1(input_list):
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum


print proc1(range(1,1000))

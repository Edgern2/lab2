import Lab2

def find_min_max():
    test = [1,31,69,100]
    assert[1,100] == Lab2.calc_min_max_temperature(test)

def calc_average():
    test = [1,31,69,100]
    assert[50.25] == Lab2.calc_average(test)

def calc_median():
    test = [1,31,69,100]
    assert[50] == Lab2.calc_median_temperature(test)
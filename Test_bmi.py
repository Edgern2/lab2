import Lab2

print("Test Lab2")

def test_bmi_normal_weight():

        result = 0
        BMI = Lab2.calculate_bmi(69,1.73)
        assert(result == BMI)


def test_bmi_over_weight():

        result = 1
        BMI = Lab2.calculate_bmi(100,1.73)
        assert(result == BMI)


    

def test_bmi_under_weight():

        result = -1
        BMI = Lab2.calculate_bmi(10,1.73)
        assert(result == BMI)
        


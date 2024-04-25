def calculate_bmi(h,w):
    print("Height = "+ str(h))
    print("Weight = "+ str(w))
    H=h*h
    BMI=w/H
    print("Your BMI =" + str(BMI))
    if BMI<18.5:
        print ("Skinny")
    elif 18.5<=BMI<=25.0:
        print("Normal")
    elif BMI > 25.0:
        print("Fatt")



calculate_bmi(w=69,h=1.73) 
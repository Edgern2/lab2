def calculate_bmi(w,h):
    print("Height = "+ str(h))
    print("Weight = "+ str(w))
    
    H = h * h
    BMI = w / H


    print("Your BMI =" + str(BMI))
    if BMI<18.5:
        print ("Skinny")
        return -1
    elif 18.5<=BMI<=25.0: 
        print("Normal")
        return 0
    elif BMI > 25.0:
        print("Fat")
        return 1



calculate_bmi(w=69,h=1.73) 
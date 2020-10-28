height = float(input("WRITE YOUR HEIGHT"))
weight = float(input("WRITE YOUR WEIGHT"))
b  = pow(height/100, 2)
a = 0
BMI = weight / b
ideal_weight = b * a

if BMI < 18.49:

    a = 18.49

    ideal_weight = b * a

    print("You're below of your ideal weight you should get ", round(abs(weight - ideal_weight), 2), "kilos and your BMI is ", round(BMI, 2))

elif BMI >= 18.4 and BMI < 24.99:

    print("Your BMI is normal and equal to", round(BMI, 2))

elif BMI >= 24.99 and BMI < 29.99:

    a = 24.99

    ideal_weight = b * a

    print("You're above of your ideal weight you should give", round(abs(weight - ideal_weight), 2), "kilos"
                                                                                                     "and your BMI is", round(BMI, 2))
else:
    print("DANGER")

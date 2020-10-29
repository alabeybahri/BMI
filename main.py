def calculateBmi(weight, height):
    return weight / pow(height/100, 2)

def calculateIdealWeight(height, weight_limit):
    return pow(height/100, 2) * weight_limit

bmi_lower_bound = 18.49
bmi_middle_bound = 24.99
bmi_higher_bound = 29.99

weight_limit = 0
ideal_weight = 0

height = float(input("WRITE YOUR HEIGHT(cm): "))
weight = float(input("WRITE YOUR WEIGHT(kg): "))

BMI = calculateBmi(weight, height)

if BMI < bmi_lower_bound:
    ideal_weight = calculateIdealWeight(height, bmi_lower_bound)
    print("You're below of your ideal weight you should get ", round(abs(weight - ideal_weight), 2), "kilos and your BMI is ", round(BMI, 2))

elif bmi_lower_bound <= BMI < bmi_middle_bound:
    print("Your BMI is normal and equal to", round(BMI, 2))

elif bmi_middle_bound <= BMI < bmi_higher_bound:
    ideal_weight = calculateIdealWeight(height, bmi_middle_bound)
    print("You're above of your ideal weight you should give", round(abs(weight - ideal_weight), 2), "kilos"
                                                                                                     " and your BMI is", round(BMI, 2))
else:
    print('DANGER')
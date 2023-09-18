# This is simple program that i read for my python training. It is used to calculate bmi.

def getData():
    weight = float(input("Please, enter your weight in kg: "))
    height = float(input("Please, enter your height in meters: "))
    return weight, height

def summary(bmi):
    if bmi < 18.5:
        print("Your bmi is too low. You are underweight, you should eat more.")
    elif bmi > 18.5 and bmi < 24.9:
        print("Your bmi is in normal range. Keep it up!")
    elif bmi > 25 and bmi < 29.9:
        print("Your bmi is a little to hight. You are overweight. You should make some work out!")
    elif bmi > 30 and bmi < 34.9:
        print("Your bmi is definitely too hight. You have to go to the gym instantly!")
    elif bmi > 35:
        print("Your bmi is extremely hight. If you don't do something, you will have a problem.")
    

def main():
    w, h = getData()
    bmi = w / (h * h)
    print(f'Your bmi is {bmi}')
    summary(bmi)



main()
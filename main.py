boy = float(input("Bo'yingizni metrlarda kiriting (masalan: 1.75): "))
vazn = float(input("Vazningizni kilogrammlarda kiriting (masalan: 70): "))

bmi = vazn / (boy ** 2)

print(f"Sizning BMI qiymatingiz: {bmi:.2f}")

if bmi < 18.5:
    print("Siz ozg'insiz (Underweight).")
elif 18.5 <= bmi < 24.9:
    print("Sizning vazningiz normal (Normal weight).")
elif 25 <= bmi < 29.9:
    print("Siz ortiqcha vaznga egasiz (Overweight).")
else:
    print("Siz semiz toifasidasiz (Obese).")

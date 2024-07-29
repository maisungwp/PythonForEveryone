w = float(input("please input weight (kg): "))
h = float(input("please input height (cm): "))
h = h / 100
bmi = w / h**2

print(bmi)
if 0 < bmi < 20:
    print("thin")
else:
    if bmi > 25:
        print("fat")
    else:
        print("normal")

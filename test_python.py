# เครื่องคำนวณอายุที่เหลืออยู่
class Calculator:
    def ageCalculator():
        # รับอายุ
        age = input("Please insert your age: ")

        # กระบวนการ
        restedAge = 80 - age

        restedAgeRatio = restedAge / 80

        print("This man have", restedAge, "Years")

        if restedAgeRatio >= 0.8:
            print("Young People")
        elif restedAgeRatio <= 0.2:
            print("Old People")
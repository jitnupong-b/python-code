class GradeCalculator:

    def __init__(self):
        self.__grade = 'F'

    def calculate(self, score):
        if score > 80:
            self.__grade = 'A'
        elif score > 70:
            self.__grade = 'B'
        elif score > 60:
            self.__grade = 'C'

    def showGrade(self):
        print("Your Grade is: ", self.__grade)

myCalculator = GradeCalculator()
myCalculator.showGrade()

myCalculator.calculate(75)
myCalculator.showGrade()
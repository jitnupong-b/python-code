# จงเขียนโปรแกรมที่มีการรับค่าจากผู้ใช้เป็นชื่อ
# จากนั้นทำการตรวจสอบว่าตรงกับ Harrison หรือไม่
# โดยให้โอกาสการทายของผู้ใช้เท่ากับ จำนวนอักขระในชื่อที่เป็นผลเฉลย

name = input("Guess the name:")

for i in range(8):
    
    if name == 'Harrison':
        print("Congratulations")
        break
    else:
        print("Sorry")
        name = input("Guess the name again:")
        

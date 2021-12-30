#  ตัวอย่างการใช้ range() สั่งให้เริ่มต้นที่ 0 --> 9 คือ 10 ตัว
for i in range(10):
    print(i)

print()

# เริ่มที่ 1 --> 9 คือ 9 ตัว 
for i in range(1, 10):
    print(i)

print()

# เริ่มที่ 1 --> 9 คือ 9 ตัว แต่กระโดดที่ละ 2
for i in range(1, 10, 2):
    print(i)

print()

# เริ่มที่ 10 --> 0 แต่ไม่เอา 0 โดยกระโดดทีละ -1
for i in range(10, 0, -1):
    print(i)
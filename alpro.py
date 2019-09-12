listgpa = [3, 2.7, 2.5, 4]
for gpa in listgpa :
    print(gpa)

def bonus(input):
        bonus = 500000
        x = input * bonus
        return x

for gpa in listgpa:
    print(gpa)
    if gpa > 3:
        print("Selamat anda mendapatkan bonus sebesar Rp.", bonus(gpa))
    else:
        print("Maaf anda tidak mendapatkan bonus")
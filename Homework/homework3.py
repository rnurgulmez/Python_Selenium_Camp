students = ["ahmet", "mehmet", "ali", "veli", "ayşe"]
print(students)

print("**********************")

# listeye kullanıcının girdiği ismi ekledik
newStudent = input("Eklemek istediğiniz öğrencinin adını giriniz : ")
students.append(newStudent)
print(students)

print("**********************")

# listeden kaldırılmak istenen ismi kaldırdık
removeStudent = input("Kaldırmak istediğiniz öğrencinin adını giriniz : ")
students.remove(removeStudent)
print(students)

print("**********************")

# listeye birden fazla öğrenci eklemek
number = int(input("Kaç adet öğrenci eklemek istiyorsunuz? :"))
i = 0
while i < number:
    newStudent1 = input("Eklemek istediğiniz öğrencinin adını giriniz :")
    i += 1
    students.extend([newStudent1])
print(students)

print("**********************")

# listedeki tüm öğrencileri tek tek ekrana yazdıran fonksiyon


def showList():
    for student in students:
        print(student)


# fonksiyonu çağırdık
showList()

print("**********************")

# istenilen öğrencini öğrenci numarasını(indexi öğrenci numarası kabul ederek) öğrenmemizi sağlayan fonksiyon


def showStudentNo():

    studentName = input(
        "Numarasını öğrenmek istediğiniz öğrencinin adını giriniz : ")
    for student in students:
        if studentName == student:
            print(
                f"{student} adlı öğrencinin numarası {students.index(student)}")


# fonksiyonu çağırdık
showStudentNo()

print("**********************")

# birden fazla öğrenciyi silmeyi mümkün kılan fonksiyon


def removeStudents():
    number = int(input("Kaç kişiyi silmek istersiniz? :"))
    newList = []
    i = 0
    while i < number:
        removedStudent = input("Silinmesini istediğiniz öğrencinin adı : ")
        i += 1
        newList.append(removedStudent)

        for student in students:
            if student in newList:
                students.remove(student)
    print(students)


# fonksiyonu çağırdık
removeStudents()

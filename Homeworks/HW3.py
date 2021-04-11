#İnputları alıyor
student_number=int(input("Kaç öğrenci var ?"))
student_grades= dict() 
for i in range(student_number):
    
    isim= str(input("isim:"))
    puan1=int(input("vize:"))
    puan2=int(input("proje:"))
    puan3=int(input("final:"))
    student_grades[isim]=[puan1,puan2,puan3]
    


#İşlem yaparak value sonuna ekliyor
for k in student_grades.keys():
    grades=student_grades[k]
    passing_grade=grades[0]*(0.3)+grades[1]*(0.3)+grades[2]*(0.4)
    student_grades[k].append(passing_grade)
    print("İsim:",k +",","Geçme Notu:","{:.2f}".format(passing_grade))


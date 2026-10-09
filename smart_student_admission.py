# Smart Student Admission System

print("------------------------------------")
print("|  Smart Student Admission System  |")
print("------------------------------------\n")

student_name = input("Enter Student Name : ")
age = input("Enter Age : ")
metric = input ("Enter Matric percentage : ")
inter = input("Enter Intermediate percentage : ")
test_score = input("Entry test score : ")
domicile = input("Do you have Domicile (Yes/No) : ")

print()

#Basic Eligibility check:
if age.isdigit() and metric.isdigit() and inter.isdigit() and test_score.isdigit():
    age = int(age)
    metric = int(metric)
    inter = int(inter)
    test_score = int(test_score)

    #AGE
    if age >=17:
        pass
    else:
        print(f"Your Age {age}, Minimum age required 17.\n")
    #Metric    
    if metric >= 60:
        pass
    else:
        print(f"Your Metric Percentage {metric}, Minimum Percentage required 60%.\n")

    #inter
    if inter >= 60:
       pass
    else:
        print(f"Your Intermediate Percentage {inter}, Minimum Percentage required 60%.\n")
    #test_score
    if test_score >= 50:
        pass
    else:
        print(f"Your test score is {test_score}, But Required at least 50.\n")    
    #Domicile
    if domicile.lower() =="yes":
        pass
    else:
        print("Domicile Required")
    #check user data in to required data 
    # Eligible     
    if age >=17 and metric >= 60 and inter >= 60 and  test_score >= 50 and domicile.lower() =="yes":  
        pass
        #Excellient Scholarship
        if inter >= 85 and inter <= 100 and test_score >=85 and test_score <=100:
            admission_status = True
            merit = "Excellient"
            Excellent_Merit = 50
            print("------------------------")
            print("|  Eligibility Status  |")
            print("------------------------\n")

            print(f"Name = {student_name}")
            print(f"Age = {age}")
            print(f"Intermediate percentage = {inter}")
            print(f"Test score = {test_score}")
            print(f"Admission Status = {admission_status}")
            print(f"Merit Category = {merit}")   
            print(f"Scholarship = {Excellent_Merit}%\n")

        #Good Scholarship
        elif inter >= 70 and inter < 85 and test_score >=70 and test_score < 85:
            admission_status = True
            merit = "Good Merit"
            Good_Merit = 25
            print("------------------------")
            print("|  Eligibility Status  |")
            print("------------------------\n")


            print(f"Name = {student_name}")
            print(f"Age = {age}")
            print(f"Intermediate percentage = {inter}")
            print(f"Test score = {test_score}")
            print(f"Admission Status = {admission_status}")
            print(f"Merit Category = {merit}")   
            print(f"Scholarship = {Good_Merit}%\n")

        #Normal Scholarship  
        elif inter >= 60 and inter < 70 and test_score >=50 and test_score < 70:
            admission_status = True
            merit = "Normal Merit"
            Normal_Merit = "No Scholarship"
            print("------------------------")
            print("|  Eligibility Status  |")
            print("------------------------\n")


            print(f"Name = {student_name}")
            print(f"Age = {age}")
            print(f"Intermediate percentage = {inter}")
            print(f"Test score = {test_score}")
            print(f"Admission Status = {admission_status}")
            print(f"Merit Category = {merit}")   
            print(f"Scholarship = {Normal_Merit}\n")    
                                           
    else:    
        print(f"Dear {student_name}, You're not Eligible.")

else:
    print("Invalid Command.\n")
    

print("نظام ادارة درجات الطلاب")

students_number= int(input("How many students ?"))

student_marks= int(input("Enter student marks ?"))

def clou_sum(mark1, mark2, mark3, mark4):
    total = mark1, mark2, mark3, mark4
    return total

def clou_Agv(total):
    Avg = total //4
    return Avg

def clo_Resut(Avg):
    if Avg >= 90:
        return "Result : Excellent"
    elif Avg >= 75 :
        return " Result : Very good"
    elif Avg >= 60 :
        return "Result : Good"
    elif Avg >= 50:
        return "Result : Pass "
    else:
        return "Result :Fail"
    
for averages in Avg:          
    if Avg >= 50:
       print ("Pass +i=1")
    else:
        print ("Fail +=1")
        
highest_degree = max(Avg)

the_average_drgrees = sum(Avg) / students_number

print("=================Student Report==================================")
student_name = input ("Enter Student Name :")
mark1 = float (input("Enter First Subject mark :"))
mark2 = float (input("Enter Second Subject mark :"))
mark3 = float (input("Enter Thired Subject mark :"))
mark4 = float (input("Enter Final Subject mark :"))
total = clou_sum(mark1, mark2, mark3, mark4)
Avg =  clou_Agv(total)
Result =   clo_Resut(Avg)
    
print("======================Result=======================================")
print ("Student Name :" , student_name)
print ("Total :" ,total )
print ("Average :", Avg)
print ("Student result :", Result)
print ("-----------------------------------------------------------------")

print("Total Students :" ,students_number)
print("-----------------------------------------------------------------")
for averages in Avg:          
    if Avg >= 50:
       print ("Pass +=1")
    else:
        print ("Fail +=1")

print ("highest Grade:",highest_degree)

print ("Average:",the_average_drgrees )

print ("-----------------------------------------------------------------")

print("--------------------Student data----------------------------------")
while True:
    name= input("student name")
    if name == student_name :
        break 
    while True:
        try: 
            grade = float (input("enter student grade"))
            if grade == Result:
                break
            else:
                print ("wrong")


      



    
    
    
     
   
        


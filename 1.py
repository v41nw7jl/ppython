#'name', 'marks' and do the following: i. Accept the details of 10 students and display it.
#ii. Search & Display the details of a student on the basis of its rollno.
#iii. Display the details of topper student.

stu={101:['Amit',90],102:['Shaam',95]}

for i in range(2):
    rollno=int(input("Enter your roll no"))
    name=input("Enter your name")
    marks=int(input("Enter your marks"))
    print("rollno:",rollno,":","name:",name,":","marks:",marks)
print(stu(rollno))

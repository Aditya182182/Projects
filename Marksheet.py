name = input("Enter student name: ")
add = input("Enter student address: ")

subjects = []
for i in range(5):
    subject_name = input("Enter subject {} name: ".format(i + 1))
    marks = float(input("Enter marks obtained in {}: ".format(subject_name)))
    subjects.append((subject_name, marks))

total_marks = 500
obtained_marks = 0
for subject, marks in subjects:
    total_marks += 100  
    obtained_marks += marks
# total_marks=500   
# obt_marks=subject_name
# percentage=obt_marks/total_marks*100

# percentage = (obt_marks / total_marks) * 100
print("                                                Your name :", name)
print("                                                Address: ",add)
print("============================================================================================================================")
print("Subject                    |Total Marks           |Obtain Marks                           |Percentage")
print("============================================================================================================================")
print("Maths                      |100                   |",subject,"                                 |",marks)
print("Physics                    |100                   |",subject,"                                 |",marks)
print("Chemistry                  |100                   |",subject,"                                 |",marks)
print("Biology                    |100                   |",subject,"                                 |",marks)
print("English                    |100                   |",subject,"                                 |",marks)
print("============================================================================================================================")
print("Total                      |500                   |",obtained_marks ,"                                |",percentage)



name = input("Enter student name: ")
add = input("Enter student address: ")

subjects = {}
all_marks = []
for i in range(5):
    subject_name = input("Enter subject {} name: ".format(i + 1))
    marks = int(input("Enter marks obtained in {}: ".format(subject_name)))
    print(type(marks))
    subjects[subject_name] = marks
    all_marks.append(marks)



total_marks=500   
obt_marks=sum(all_marks)
percentage=obt_marks/total_marks*100
percentage = (obt_marks / total_marks) * 100



print("                                                Your name :", name)
print("                                                Address: ",add)
print("============================================================================================================================")
print("Subject                    |Total Marks           |Obtain Marks                           |Percentage")
print("============================================================================================================================")
for subject_name, marks in subjects.items():
    print(f"{subject_name}               |100                   |{marks}                                  |{marks/100*100}")

print("============================================================================================================================")
print("Total                      |500                   |",obt_marks ,"                                |",percentage)



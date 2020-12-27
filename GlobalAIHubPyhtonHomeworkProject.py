  
_try = 3
correct_name= "huseyinmutlu".upper()
while(True):
    name = input("Please write your name: bkz (huseyin) ")
    surname = input("Please write your surname: bkz(mutlu ")
    full_name = (name + surname).upper()
    if(full_name != correct_name):
        print("Name is wrong.\n\n")
        _try-=1
        if(_try ==0):
            print("Please try again later.\n\n")
            break
    else:
        break
if(_try !=0):
    lessons_list = ["C++","Ruby","Python","Java","Html","R"]
    student_lessons = list()
    print("Please choose 3-5 lessons\n")
    for i in range(len(lessons_list)):
        print(str(i+1) + ". "+ lessons_list[i] )
    print("\n")

    for i in range(len(lessons_list)):
        if(len(student_lessons)!=5):
            lesson = int(input(str(i+1)+". choose(0-1-2-3-4-5-6): "))
            if(lesson>=0 and lesson<8):
                if(lesson ==0 and len(student_lessons)>=3):
                    break
                elif(lesson ==0 and len(student_lessons)<3):
                    print("\nYou failed in class\n\n")
                    break 
                student_lessons.append(lessons_list[lesson-1])
            else:
                print("Please select within the specified range\n")
        else:
            print("You can choose a maximum of 5 lessons\n")
            break

    if(len(student_lessons)>=3):
        print("\n")
        for i in range(len(student_lessons)):
            print(str(i+1) + ". "+ student_lessons[i] )
        exam_lesson = int(input("Which course do you want to take the exam?\n")) 
        chosen_course = student_lessons[exam_lesson-1]
        midterm = int(input("Please enter the midterm exam grade of "+chosen_course+" : "))
        final = int(input("Please enter the final exam grade of "+chosen_course+" : "))
        project = int(input("Please enter the project grade of "+chosen_course+" : "))
        grades = (midterm * 0.3) + (final * 0.5) + (project * 0.2)
        print("\n\nYour total grades "+ str(grades))
        if(grades >= 90):
            print("AA")
        elif(grades >=70 and grades<90):
            print("BB")
        elif(grades >=50 and grades<70):
            print("CC")
        elif(grades >=30 and grades<50):
            print("DD")
        elif(grades <30):
            print("FF")
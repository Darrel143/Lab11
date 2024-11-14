name = input("Enter your name: ")
section = input("enter your section: ")

#Check and validate prelim grade
prelim = float(input("Enter Prelim Grade: "))
if prelim < 40 or prelim > 100:
    print("Invalid grade for prelim")
else:
    print(f"Grade for prelim: {prelim:.2f}")
    
#Check and validate midterm grade
midterm = float(input("Enter your Midterm grade: "))
if midterm < 40 or midterm > 100:
    print("Invalid grade for midterm")
else:
    print(f"Grade for midterm: {midterm:.2f}")
    
#Check and validate finals grade
finals = float(input("Enter your Finals grade: "))
if finals < 40 or finals > 100:
    print("Invalid grade for finals")
else:
    print(f"Grade for finals: {finals:.2f}")

#Calculate total grade only if all grades are valid
if (40 <= prelim <=100) and (40 <= midterm <=100) and (40 <= finals <= 100):
    total_grade = round((prelim * 0.33) + (midterm * 0.33) + (finals * 0.33))
    print(f"Total Grade: {total_grade}")
    
    #Display the grade points
    if 98 <= total_grade <= 100:
        print("Grade Points: 1.00 Excellent")
    elif 96 <= total_grade <= 97:
        print("Grade Points: 1.25 Outstanding")
    elif 93 <= total_grade <= 95: 
        print("Grade Points: 1.50 Superior")   
    elif 90 <= total_grade <=92:
        print("Grade Points: 1.75 Very Good")
    elif 87 <= total_grade <=89:
        print("Grade Points: 2.00 Good")
    elif 84 <= total_grade <=86:
        print("Grade Points: 2.25 Satisfactory")
    elif 81 <= total_grade <= 83: 
        print("Grade Points: 2.50 Fairly Satisfactory")
    elif 78 <= total_grade <= 80:
        print("Grade Points: 2.75 Fair")
    elif 75 <= total_grade <= 77:
        print("Grade Points: 3.00 Passed")
    else:
        print("Grade Points: 5.00 Failed")
else:
    print("Invalid grades")
class student:
  
 def __init__(self, name,roll_number, CGPA):
  self.name =name
  self.roll_number =roll_number
  self.CGPA =CGPA 

def sort_students(student_list):
   sorted_students =sorted(student_list, 
                           key=lambda student: 
  student.CGPA, reverse =True)
   return sorted_students
students = [student("hari", "A123", 7.8),
          student("saranya", "A124", 9.5),
          student("raja","A125", 8.5),
          student("roja", "A126", 7.5)
          ]

sorted_students = sort_students(students)
for student in sorted_students:
  print("name: {}, roll number: {}, CGPA: {}". format(student.name, student.roll_number, student.CGPA))
	# Student = (name, grade, age)
2	class student:
3	    def __init__(self, name, grade, age):
4	        self.name = name
5	        self.grade = grade
6	        self.age = age
7	    
8	    
9	    def __str__(self):
10	        student_str=( '\n\nNAME : ' + self.name +
11	                    '\nGRADE : ' + self.grade +
12	                    '\nAGE : ' + self.age )
13	        return student_str
14	        
15	        
16	
17	student_a = student("bob", "1", "5")
18	print("Printing the student a details")
19	print(student_a)
20	
21	student_b = student("joe", "2", "6")
22	print("Printing the student b details")
23	print(student_b)

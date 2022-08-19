# Class 1
class Student:
  student_id = "1234"
  gender ="Male"
  date_of_Birth ="08/08/2000"
  first_name = "Naga"
  middle_name = "Sai"
  last_name = "Srinivas"
  other_student_details = "NA"

# Class 2
class courses_offered:
  course_offering_id = "123456"
  course_offering_name = "NA"
  other_course_offering_details = "NA"

# Class 3
class course_scheduled(Courses_offered):
  course_schedule_id = "xyz"
  course_schedule_details = "abc"
  def course_offering_id(self):
    self.course_offering_id

# Class 4
class Student_Course_Registeration(Student_id,course_scheduled):
  def __init__(self):
    self.course_schedule_id
    self.student_id

# Class 5
class Staff:
    staff_id = "452512"
    gender = "Male"
    date_of_birth = "18/09/12"
    first_name = "ABCDEF"
    last_name = "GHIJKL"
    job_title = "professor"
    phone_number = "9493066512"
    email_address = "xyz@gmail.com"
    other_staff_details = "Contact_college"



# Class 6
class Staff_Course_Supervision(Staff,courses_offered):
   def __init__(self):
    self.staff_id
   def course_id(self):
    self.course_offering_id

# Class 7
class Staff_Research_Interests(Staff):
  Area_of_Research_ID = "8598"
  def __init__(self):
    self.staff_id

# Class 8
class Research_Projects:
  Project_Id = "25455"
  Project_Name = "research X"
  Project_Description = "NA"
  Other_Details = "Contact Project Mentor"

# Class 9
class Staff_on_Research_Projects(Staff,Research_Projects):
  def __init__(self):
    self.Project_Id
    self.staff_Id
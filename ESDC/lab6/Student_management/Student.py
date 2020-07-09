class Student:
    
    def __init__(self, name, birth_year, gender):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender

    def get_id(self):
        return self.student_id
    
    def get_name(self):
        return self.name

    def get_birth_year(self):
        return self.birth_year

    def get_gender(self):
        return self.gender

    def push_id(self, course_id):
        self.student_id = course_id

    def edit(self, name, birth_year, gender):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender

    def to_string(self):
        return "ID: " + str(self.student_id) + ", Name: " + str(self.name) + ", Birth year: " + str(self.birth_year) + ", Gender: " + str(self.gender)

    
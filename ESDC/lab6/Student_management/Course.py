class Course:
    
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.course_id
    
    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def push_id(self, course_id):
        self.course_id = course_id

    def edit(self, name, credit):
        self.name = name
        self.credit = credit

    def to_string(self):
        return "ID: " + str(self.course_id) + ", Name: " + str(self.name) + ", Credit: " + str(self.credit)

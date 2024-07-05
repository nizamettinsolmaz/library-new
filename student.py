from person import Person

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)

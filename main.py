class StudentsInMLOps:
    def __init__(self):
        self.total_students = 1

    def enrollStudents(self, num):
        self.total_students += num

    def dropStudents(self, num):
        self.total_students -= num

    def getTotalStrength(self):
        return self.total_students

    def getClassName(self):
        return self.__class__.__name__

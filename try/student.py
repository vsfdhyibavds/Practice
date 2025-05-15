total_students = 0
class Student:
    def __init__(self, first_name, last_name,age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        Student.total_students += 1

        @property
        def email(self):
            return self._first_name

        # getter method for the first name
        @property
        def first_name(self):
            return self._first_name

        # setter method
        @first_name.setter
        def first_name(self, fname):
            if isinstance(fname, str):
                self.first_name = fname
            else:
                raise ValueError("Firstname has to be a string")

            #getter method
            @property
            def last_name(self):
             return self._last_name

        #setter methods
        @last_name.setter
        def last_name(self,lname):
            if isinstance(lname, str):
                self._last_name = lname
            else:
                raise ValueError("Lastname has to be a string")

            #string presentation
            def __repr__(self):
                return str(self.__dict__)


            Student_1 = Student("John", "Doe", 23, "Male")
            Student_2 = Student("Janee","Wong", 22, "Female")
            Student_3 = Student("Alex ", "Wahome", 30, "Male")

            #class variables and methods

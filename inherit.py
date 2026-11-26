class user:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(user):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


stu1 = Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()

# the other way wont work that is users class object wont be able to inherit the methods from Student class


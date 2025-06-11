#assignment :student grade tracker
#build a student class with:
#attributes: name, student ID, GPA
#methods: display student info,checkif student is pass or not(GPA>2)

class student:
    def __init__(self,stdname,stdid,gpa):
        self.stdname = stdname
        self.stdid = stdid
        self.gpa = gpa

    def display(self):
        print(f"{self.stdname}'s id is {self.stdid}.the gpa is{self.gpa}")

    def checkgpa(self):
        if(self.gpa>2):
            print(f"{self.stdname }has passed the exam")
        else:
            print(f"{self.stdname }has failed the exam")






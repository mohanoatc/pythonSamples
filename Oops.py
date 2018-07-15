students = []

class Mohan:
    school = "sai public school"
    def __init__(self,std,number=1):
        # student={"name":std,"number":number}
        self.name=std
        students.append(self)
    def __str__(self):
        return "rajarammohanrai ".capitalize() + self.name.capitalize()
    def do_cap (self):
        return self.name.capitalize()

mohan = Mohan("mohanRam4")
#mohan.student("mohanRam", 1122)
print(mohan)
print(mohan.do_cap())
print(Mohan.school.capitalize())

class Mohannew(Mohan):
    school = "sai school"

    def do_cap(self):
        sample = super().do_cap()
        return sample+"New"

newMohan = Mohannew("mohanNew")
print(newMohan.do_cap())

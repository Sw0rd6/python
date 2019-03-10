class Student:
    def __init__(self,Stu_id,Name,Sex,Age):
        self.Stu_id = Stu_id
        self.Name = Name
        self.Sex = Sex
        self.Age = Age
    def show(self):
        print("%-16s\t%-16s\t%-16s\t%-4d\t"%(self.Stu_id,self.Name,self.Sex,self.Age))
    def showtime(self):
        f = open("/home/honorwh/sms.csv","a")
        f.write("%s\t%-16s\t%-16s\t%d\n"%(self.Stu_id,self.Name,self.Sex,self.Age))
        f.close()
#s=Student("60","a","男","20")
#s.show()
class StudentList:
    def __init__(self):
        self.students = []
    def show(self):
        print("%-16s\t%-16s\t%-16s\t%-16s\t"%("Stu_id","Name","Sex","Age"))
        for s in self.students:
            s.show()
    def __insert(self,s):
        i = 0
        while (i < len(self.students) and s.Stu_id > self.students[i].Stu_id):
            i = i + 1
        if (i < len(self.students) and s.Stu_id == self.students[i].Stu_id):
            print(s.Stu_id + '已经存在')
            return False
        self.students.insert(i,s)
        print("增加成功")
        return True
    def __update(self,s):
        flag = False
        for i in range(len(self.students)):
            if (s.Stu_id == self.students[i].Stu_id):
                self.students[i].Name = s.Name
                self.students[i].Sex = s.Sex
                self.students[i].Age = s.Age
                print("修改成功")
                flag = True
                break
            if (not flag):
                print("没有这个学生")
            return flag
    def __delete(self,Stu_id):
        flag = False
        for i in range(len(self.students)):
            if (self.students[i].Stu_id == Stu_id):
                del self.students[i]
                print("删除成功")
                flag = True
                break
            if (not flag):
                print("没有这个学生")
            return flag
    def insert(self):
        Stu_id = input("Stu_id=")
        Name = input("Name=")
        while True:
            Sex = input("Sex=")
            if (Sex=='男' or Sex=='女'):
                break
            else:
                print("Sex is not valid")
        Age = input("Age=")
        if (Age==""):
            Age = 0
        else:
            Age = int(Age)
        if Stu_id != "" and Name != "":
            self.__insert(Student(Stu_id,Name,Sex,Age))
            self.__save(Student(Stu_id,Name,Sex,Age))
        else:
            print("学号,姓名不能为空")
    def update(self):
        Stu_id = input("Stu_id=")
        Name = input("Name=")
        while True:
            Sex = input("Sex=")
            if (Sex=='男' or Sex=='女'):
                break
            else:
                print("Sex is not valid")
        Age = input("Age=")
        if (Age==""):
            Age = 0
        else:
            Age = int(Age)
        if Stu_id != "" and Name != "":
            self.__update(Student(Stu_id,Name,Sex,Age))
        else:
            print("学号,姓名不能为空")
    def delete(self):
        Stu_id = input("Stu_id=")
        if (Stu_id != ""):
            self.__delete(Stu_id)
    def __save(self,s):
        j = 0
        while (j < len(self.students)):
            j = j + 1
        self.ls = []
        self.ls.insert(j,s)
        for k in self.ls:
            k.showtime()
    def process(self):
        while True:
            s = input(">")
            if (s == "show"):
                self.show()
            elif (s == "insert"):
                self.insert()
            elif (s == "update"):
                self.update()
            elif (s == "delete"):
                self.delete()
            elif (s == "save"):
                self.save()
            elif (s == "exit"):
                break
            else:
                print("show:    show students")
                print("insert:  insert a new student")
                print("update:  update the student's message")
                print("delete:  delete a student")
                print("save:    save the results")
                print("exit:    exit the sys")
st = StudentList()
f = open("/home/honorwh/sms.csv","a")
f.write("%-16s\t%-16s\t%-16s\t%-16s\n"%("Stu_id","Name","Sex","Age"))
f.close()
st.process()
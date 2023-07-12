
def login(request):
    msg=""
    if request.POST:
        uname=request.POST.get("email")
        password=request.POST.get("password")
       
        print(uname)
        print(password)
        query="select * from login where uname='"+str(uname)+"' and password='"+str(password)+"'"
        c.execute(query)
        data=c.fetchone()
        print(data)
        if data:
            if data[2]=='admin':
                return ("/adminhome/")
            elif data[2]=='employee':
                    c.execute("select employeeid from employeereg where email='"+str(request.session['uname'])+"'")
                    owner=c.fetchone()
                    return ("/employeehome/")
            else:
                    msg="invalid username or passw0rd"
           


                    return render(request,"common/login.html",{"msg":msg})
                

        elif data[2]=='HR':
                a="select uid from userreg where email='"+str(uname)+"'"
                c.execute(a)
                userid=c.fetchone()
                print(a)
                print(userid)
                request.session['userid']=userid[0]
                return ("/userhome/")
        else:
            msg="invalid username or password"
           


    return render(request,"common/login.html",{"msg":msg})




class Employee:
    def __init__(self, employee_id, name, email):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.leave_balance = []  # Stores the balance of different types of leaves for the employee
        self.attendance = []  # Stores the attendance records of the employee

    def edit_profile(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    def request_leave(self, leave_type, start_date, end_date, reason):
        leave_request = LeaveRequest(leave_type, start_date, end_date, reason)
        

    def apply_leave_balance(self, leave_type, days):
        if leave_type in self.leave_balance:
            self.leave_balance[leave_type] += days
        else:
            self.leave_balance[leave_type] = days


class LeaveRequest:
    def __init__(self, leave_type, start_date, end_date, reason):
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason


class Attendance:
    def __init__(self, employee_id, date, status):
        self.employee_id = employee_id
        self.date = date
        self.status = status


class Admin:
    def __init__(self, admin_id, name, email):
        self.admin_id = admin_id
        self.name = name
        self.email = email

    def add_leave_type(self, leave_type):
        # Code to add a new leave type to the system


#sample employee
employee1 = Employee("001", "Alex Mathai", "alexmathai@gmail.com")

# Edit 
employee1.edit_profile(name="Alex Mathai")

# Employee requests leave
employee1.request_leave("Vacation", "2023-07-15", "2023-07-20", "Vacation trip")

# Admin adds a new leave type
admin1 = Admin("001", "Admin User", "admin@unityinfotech.com")
admin1.add_leave_type("Sick Leave")








from utils import generate_id

class User:
    def __init__(self, name, email, phone, membership_type):
        self.user_id = generate_id("U")
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type

    def to_dict(self):
        base = {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "membership_type": self.membership_type
        }
        if hasattr(self, 'roll_number'):
            base["roll_number"] = self.roll_number
        if hasattr(self, 'department'):
            base["department"] = self.department
        return base

    @classmethod
    def from_dict(cls, data):
        if data['membership_type'] == 'Student':
            return Student(data['name'], data['email'], data['phone'], data['roll_number'])
        elif data['membership_type'] == 'Faculty':
            return Faculty(data['name'], data['email'], data['phone'], data['department'])
        else:
            return cls(data['name'], data['email'], data['phone'], data['membership_type'])


class Student(User):
    def __init__(self, name, email, phone, roll_number):
        super().__init__(name, email, phone, membership_type="Student")
        self.roll_number = roll_number

    def __str__(self):
        return f"Student: {self.name} (Roll: {self.roll_number})"


class Faculty(User):
    def __init__(self, name, email, phone, department):
        super().__init__(name, email, phone, membership_type="Faculty")
        self.department = department

    def __str__(self):
        return f"Faculty: {self.name} (Dept: {self.department})"
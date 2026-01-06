from pydantic import BaseModel, EmailStr, Field

from typing import Optional 

class User(BaseModel):
    name : str

print('--'*50)
user = User(name="Alice")
print(user)

student = {"name": "John"}
student_obj = User(**student)
print(student_obj)


print('--'*50)
# set default values
class UserWithDefault(BaseModel):
    name: str = "Hasnain"
    age: Optional[int] = None
    email : Optional[EmailStr] = None
    cgpa : Optional[float] = Field(None, ge=0, le=4.0, description="CGPA out of 4.0")

user_default = UserWithDefault()
print(user_default)
print(user_default.name)
print('--'*50)

user1 = UserWithDefault(name="Jack", age='17', email="abc@example.com", cgpa=3.5)
print(user1)

u1_dict = dict(user1)
print(u1_dict)

u1_json = user1.model_dump_json()
print(u1_json)
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from passlib.hash import bcrypt


class Tasks(models.Model):
    id = fields.IntField(pk=True)
    description = fields.CharField(max_length = 50)
    is_done = fields.BooleanField(default = False)
    due_date = fields.data.DateField()
    add_date = fields.data.DatetimeField(auto_now_add = True)
    done_date = fields.data.DateField(null = True)
    done_on_time = fields.BooleanField(null = True)
    archived = fields.BooleanField(default = False)

    class Meta:
        table = "tasks"

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length = 25, unique = True)
    hashed_password = fields.CharField(max_length = 100)

    def verify_password(self, password):
        return bcrypt.verify(password, self.hashed_password)

    class Meta:
        table = "users"


Task_Pydantic = pydantic_model_creator(Tasks)
User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly = True)



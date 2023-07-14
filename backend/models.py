from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Tasks(models.Model):
    id = fields.IntField(pk=True)
    description = fields.CharField(max_length=50)
    is_done = fields.BooleanField(default = False)


Task_Pydantic = pydantic_model_creator(Tasks)


from tortoise import fields
from tortoise.models import Model


class MyModel(Model):
    key_fields = None
    data_fields = None


class User(MyModel):
    class Meta:
        table = 'users'
        table_description = 'Users :)'

    id = fields.IntField(pk=True)
    name = fields.TextField()
    username = fields.TextField()
    email = fields.TextField()
    address = fields.JSONField()
    phone = fields.TextField()
    website = fields.TextField()
    company = fields.JSONField()

    key_fields = ['id']
    data_fields = ['name', 'username', 'email', 'address', 'phone', 'website', 'company']

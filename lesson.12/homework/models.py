from tortoise import fields
from tortoise.models import Model


class MyModel(Model):
    key_fields = None
    data_fields = None

    def __str__(self):
        attrs_str = ', '.join([f'{k}={self.__getattribute__(k)}' for k in self.key_fields])
        return f'{self.__class__.__name__}({attrs_str})'

    def __repr__(self):
        return self.__str__()


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


class Comment(MyModel):
    class Meta:
        table = 'comments'
        table_description = 'Comments'

    id = fields.IntField(pk=True)
    postId = fields.IntField()
    name = fields.TextField()
    email = fields.TextField()
    body = fields.TextField()

    key_fields = ['id']
    data_fields = ['postId', 'name', 'email', 'body']


class Post(MyModel):
    class Meta:
        table = 'posts'
        table_description = 'Posts'

    id = fields.IntField(pk=True)
    userId = fields.IntField()
    title = fields.TextField()
    body = fields.TextField()

    key_fields = ['id']
    data_fields = ['userId', 'title', 'body']


class Album(MyModel):
    class Meta:
        table = 'albums'
        table_description = 'Albums'

    id = fields.IntField(pk=True)
    userId = fields.IntField()
    title = fields.TextField()

    key_fields = ['id']
    data_fields = ['userId', 'title']


class Photo(MyModel):
    class Meta:
        table = 'photos'
        table_description = 'Photos'

    id = fields.IntField(pk=True)
    albumId = fields.IntField()
    title = fields.TextField()
    url = fields.TextField()
    thumbnailUrl = fields.TextField()

    key_fields = ['id']
    data_fields = ['albumId', 'title', 'url', 'thumbnailUrl']


class ToDo(MyModel):
    class Meta:
        table = 'todos'
        table_description = 'ToDo\'s'

    id = fields.IntField(pk=True)
    userId = fields.IntField()
    title = fields.TextField()
    completed = fields.BooleanField()

    key_fields = ['id']
    data_fields = ['userId', 'title', 'completed']

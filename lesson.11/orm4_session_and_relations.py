from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

engine = create_engine("sqlite:///example2.db")
# engine = create_engine('oracle://sqlalchemy:sqlchemistry@192.168.19.33:1521/XE')
# engine = create_engine('postgresql+psycopg2://user:password@localhost:5432/postgres')
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

# class Profile(Base):
#     first


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)

    # def create_post(self):


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    # user_id = Column(Integer, ForeignKey("users.id"))
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    author = relationship(User, back_populates="posts")
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)

    posts = relationship("Post", secondary=posts_tags_table, back_populates="tags")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    """
    :param username:
    :return:
    """

    with Session()as loc_session:
        u = User(username=username)
        print("id before:", u.id)
        loc_session.add(u)
        loc_session.commit()
        print("id after:", u.id)
    return u


def author_posts():
    with Session() as loc_session:
        user = loc_session.query(User).filter_by(username="sam").one()
        print(user)

        loc_post = Post(title="First post!", author=user)
        loc_session.add(loc_post)
        loc_session.commit()
        print(loc_post)
        print(user.posts)

        loc_post = Post(title="Second post!")

        # user_posts: List[Post] = user.posts
        user.posts.append(loc_post)

        loc_session.commit()
        print(user.posts)


def create_tags():
    with Session() as loc_session:
        user = loc_session.query(User).filter_by(username="john").one()
        user.is_staff = True

        tags = [Tag(name=name) for name in ("news", "flask", "django", "python")]
        loc_post = Post(title="News Flask vs Django", author=user)
        loc_post.tags.extend(tags)

        loc_session.commit()

        print(loc_post, loc_post.tags)

        for tag in tags:
            print(tag, tag.posts)


def try_create():
    try:
        create_user("john")
        create_user("sam")
        author_posts()
        create_tags()
        print('Objects created')
    except Exception:
        print('Objects is about to already created')


if __name__ == "__main__":
    Base.metadata.create_all()

    with Session() as glob_session:
        try_create()

        users = glob_session.query(User).filter(
            User.id > 1,
            User.username != "john",
        ).all()

        print(users)

        posts = glob_session.query(Post).all()
        for post in posts:
            print(post, type(post.tags), post.tags)

        users_query = glob_session.query(
            User,
        ).join(
            Post,
            User.id == Post.author_id,
        ).filter(
            Post.tags.any(
                # Tag.name.ilike("new%"),
                Tag.name != "django",
            )
        )

        print()
        print()
        print(repr(users_query))
        print(users_query)
        print()
        print(users_query.all())
        print()

        posts_query = glob_session.query(
            Post,
        ).filter(
            Post.tags.any(
                # Tag.name.ilike("new%"),
                # Tag.name != "django",
                Tag.name == "flask",
            )
        )
        print()
        print()
        print(posts_query)
        print(list(posts_query))
        print([post for post in posts_query])
        print()
        print(posts_query.all())
        print()

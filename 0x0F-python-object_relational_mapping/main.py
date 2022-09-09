from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table, Text, ForeignKey


url = "mysql://michaseyi:&KqEMEbp,67UygW@localhost/tweeter"

engine = create_engine(url)

# Base = declarative_base()

# user_user = Table('user_user', Base.metadata,
#                   Column('follower_id', ForeignKey(
#                       'users.uid'), primary_key=True),
#                   Column('followee_id', ForeignKey('users.uid'), primary_key=True))


# class User(Base):
#     __tablename__ = "users"

#     username = Column(String(40))
#     uid = Column(Integer, primary_key=True)

#     followers = relationship('User', secondary=user_user,
#                              primaryjoin=uid == user_user.c.followee_id,
#                              secondaryjoin=uid == user_user.c.follower_id,
#                              backref='follower')

#     following = relationship('User', secondary=user_user,
#                              primaryjoin=uid == user_user.c.follower_id,
#                              secondaryjoin=uid == user_user.c.followee_id,
#                              backref='followee')

#     def __repr__(self):
#         return "User(name={}, uid={})".format(self.username, self.uid)


# # Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)


# session = Session()
# user1 = User(username="michael")

# user2 = User(username="tunde")
# user2.following.append(user1)
# session.add_all([user1, user2])
# session.commit()
# print(user2.following)
# print(user1.followers)
# for user in session.query(User).filter(User.username == "akldjf").all():
#     print(user)


engine = create_engine("sqlite:///some.db")


engine.execute("create database shout;")
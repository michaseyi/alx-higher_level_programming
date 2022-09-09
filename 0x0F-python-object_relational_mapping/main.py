from sqlalchemy import create_engine, inspect, Table, MetaData, text, Integer, String, ForeignKey, Column, DateTime
import MySQLdb


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


metadata = MetaData()


# employees_table = Table('employees', metadata,
#                         autoload=True, autoload_with=engine)
# network_table = Table('network', metadata,
#                       Column('network_id', Integer, primary_key=True),
#                       Column('name', String(100), nullable=False),
#                       Column('created_at', DateTime, nullable=False),
#                       Column('owner_id', Integer,
#                              ForeignKey('employees.emp_id'))

#                       )

# metadata.create_all(engine)


# network_table = Table('network', metadata, autoload=True, autoload_with=engine)
# print((network_table.columns.keys()))


inspector = inspect(engine)


for table in inspector.get_table_names():
    if 'emp_id' in map(lambda col: col['name'], inspector.get_columns(table)):
        print(table)
# print(dir(inspector))

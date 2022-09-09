from sqlalchemy import Integer,  Column, create_engine, text, Table, PrimaryKeyConstraint, ForeignKeyConstraint, MetaData


url = "mysql://michaseyi:&KqEMEbp,67UygW@localhost/tweeter"

engine = create_engine(url, echo=True)


# engine.execute("CREATE TABLE employees ("
#                "emp_id INTEGER PRIMARY KEY AUTO_INCREMENT,"
#                "emp_name VARCHAR(30)"
# ");")


# engine.execute(
#     text('INSERT INTO employees (emp_name) VALUES (:emp_name)'), emp_name="dilbert")


# conn = engine.connect()
# trans = conn.begin()
# conn.execute(
#     text('INSERT INTO employees (emp_name) VALUES (:emp_name)'), emp_name="michael")
# trans.commit()
# conn.close()


# for row in engine.execute(text("SELECT * FROM employees")).fetchall():
#     print(row[0])

metadata = MetaData()


user = Table('user', metadata, Column(
    'id', Integer), Column('height', Integer))
test_dates = Table('test_dates', metadata, Column(
    'height', Integer), Column('width', Integer),
    ForeignKeyConstraint(columns=['height', 'width'], refcolumns=[
                         'user.id', 'user.height'])
)

print(metadata.tables)



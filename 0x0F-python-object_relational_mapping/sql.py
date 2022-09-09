from sqlalchemy import create_engine, Table, MetaData, inspect

url = "mysql://michaseyi:&KqEMEbp,67UygW@localhost/hbtn_0e_0_usa"
engine = create_engine(url, echo=True)
metadata = MetaData()

inspector = inspect(engine)
city_table = Table('cities', metadata, autoload=True, autoload_with=engine)


print(city_table.c)


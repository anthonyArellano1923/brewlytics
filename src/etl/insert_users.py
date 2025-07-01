from faker import Faker
import pathlib, json, mysql.connector as mc

fake = Faker()

INSERT_SQL = """
insert into Users (
  full_name, email, phone_number, age, street, city, state, postal_code
  )
  values(
    %(full_name)s, 
    %(email)s,  
    %(phone_number)s,  
    %(age)s, 
    %(street)s, 
    %(city)s, 
    %(state)s, 
    %(postal_code)s)
"""

def getConnection():
    return mc.connect(
        host='localhost',
        user='root',
        password='ynoht519263',
        database='myBreweryDB',
        autocommit=True
    )


def main():
  
  connection = getConnection()
  cursor = connection.cursor()
  for users in range(50):
    user = {
      "full_name": fake.name(),
      "email": fake.email(),
      "phone_number": fake.phone_number(),
      "age": fake.random_int(min=18, max=80),
      "street": fake.street_address(),
      "city": fake.city(),
      "state": fake.state(),
      "postal_code": fake.postalcode()
    }
    cursor.execute(INSERT_SQL, user)
    print(f"{cursor.rowcount} filas insertadas")

if __name__ == "__main__":
  main()
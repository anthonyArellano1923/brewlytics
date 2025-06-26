import json, pathlib, mysql.connector as mc

# ------------- Rutas -------------

RAW_FILE = pathlib.Path(__file__).parents[2] / "data" / "raw" / "breweries.json" # Primero me ubico en la carpeta padre del proyecto y luego bajo hacia /data/raw/ donde está el archivo breweries_page1.json

# ------------- Crear conexión -------------

def getConnection():
    return mc.connect(
        host='localhost',
        user='root',
        password='ynoht519263',
        database='myBreweryDB',
        autocommit=True
    )

# ----------- Mapeo del JSON ---------------

INSERT_SQL = """
  INSERT INTO Brewery
     (api_id, name, brewery_type, street, city, state, postal_code,
  country, latitude, longitude, phone, website_url)
  VALUES
    (%(id)s, %(name)s, %(brewery_type)s, %(street)s, %(city)s,
    %(state)s, %(postal_code)s, %(country)s,
    %(latitude)s, %(longitude)s, %(phone)s, %(website_url)s)
  ON DUPLICATE KEY UPDATE
    name = VALUES(name), 
    brewery_type = VALUES(brewery_type),
    street = VALUES(street), 
    city = VALUES(city),
    state = VALUES(state), 
    postal_code = VALUES(postal_code),
    country = VALUES(country), 
    latitude = VALUES(latitude),
    longitude = VALUES(longitude), 
    phone = VALUES(phone),
    website_url = VALUES(website_url), 
    updated_at = NOW();
"""

def main():
    rows = json.loads(RAW_FILE.read_text())
    connection = getConnection()
    cursor = connection.cursor()

    for singleRow in rows:
      # Coloca en la columna correcta los datos que vienen con un nombre diferente desde la api
      singleRow.setdefault("street", singleRow.get("address_1"))
      singleRow.setdefault("state", singleRow.get("state_province"))

      #Ahora, con todos los campos correctamente guardados en cada fila correspondiente a esta iteración, se ejecuta el insert into a la tabla Brewery
      cursor.execute(INSERT_SQL, singleRow)
      print(f"{singleRow} Insertada.")

    print(f"{cursor.rowcount} filas insertadas/actualizadas")

if __name__ == "__main__":
   main()
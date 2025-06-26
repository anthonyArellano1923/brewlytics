import pathlib, json, mysql.connector as mc

RAW_FILE = pathlib.Path(__file__).parents[2] / "data" / "raw"

def getConnection():
    return mc.connect(
        host='localhost',
        user='root',
        password='ynoht519263',
        database='myBreweryDB',
        autocommit=True
    )

INSERT_SQL = """
  INSERT INTO Beers 
    (api_id, name, description, brewery_id, 
    image_url, abv, ibu, ebc, volume_oz)
  Values (%(id)s, %(name)s, %(description)s, %(brewery_id)s, 
          null, %(abv)s, %(ibu)s, %(ebc)s, %(volume_oz)s)
  ON DUPLICATE KEY UPDATE
    name = VALUES(name), 
    description = VALUES(description), 
    image_url = null, 
    abv = VALUES(abv), 
    ibu = VALUES(ibu), 
    ebc = VALUES(ebc), 
    volume_oz = VALUES(volume_oz),
    updated_at = NOW()
"""
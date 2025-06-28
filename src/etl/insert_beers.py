import pathlib, json, mysql.connector as mc

RAW_FILE = pathlib.Path(__file__).parents[2] / "data" / "raw" / "beers.json"

INSERT_SQL = """
  INSERT INTO Beers 
    (api_id, name, description, abv, ibu, ebc, volume_oz)
  Values (%(id)s, %(name)s, %(description)s, %(abv)s, %(ibu)s, %(ebc)s, %(volume_oz)s)
  ON DUPLICATE KEY UPDATE
    name = VALUES(name), 
    description = VALUES(description), 
    abv = VALUES(abv), 
    ibu = VALUES(ibu), 
    ebc = VALUES(ebc), 
    volume_oz = VALUES(volume_oz),
    updated_at = NOW()
"""

def getConnection():
    return mc.connect(
        host='localhost',
        user='root',
        password='ynoht519263',
        database='myBreweryDB',
        autocommit=True
    )

def trimSpecs(row): #This function returns a dict that contains only the values required by the DB
    requiredValues = ['id', 'name', 'description', 
     'abv', 'ibu', 'ebc', 'volume'] 
    newRow = {}
    for attribute in requiredValues:
        if attribute == 'volume':
          newRow['volume_oz']= round(int(row[attribute]['value']) * 0.033814)
          continue
        newRow[attribute] = row[attribute]
    return newRow

def main():
    rows = json.loads(RAW_FILE.read_text())
    connection = getConnection()
    cursor = connection.cursor()

    for singleRow in rows:
        row = trimSpecs(singleRow)
        cursor.execute(INSERT_SQL, row)
        print(f"Insertada.")

    print(f"{cursor.rowcount} filas insertadas/actualizadas")

if __name__ == '__main__':
    main()
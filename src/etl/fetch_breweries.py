import json, pathlib, requests

API_URL = "https://api.openbrewerydb.org/v1/breweries" # Guarda en una vrialbe la url de la api
RAW_DIR = pathlib.Path(__file__).parents[2] / "data" / "raw" # construye la ruta de la carpeta data/raw situada dos niveles por encima del script, sin importar dónde se ejecute el proyecto.
RAW_DIR.mkdir(parents=True, exist_ok=True) # garantiza que data/raw/ exista antes de intentar guardar el archivo, sin importar si la estructura estaba o no creada.

def main():
  all_rows = []
  page = 1
  while True:
    resp = requests.get(API_URL, params={"per_page" : 200, "page": page}) #Obtiene datos de la api, Cada página de la respuesta tendrá 200 resultados.
    resp.raise_for_status()  #Detiene si hay un error. Con eso tu script se detiene inmediatamente y muestra el motivo (404, 500, etc.) en vez de seguir trabajando con datos inválidos.
    data = resp.json() #Guarda en una variable el resultado en formato JSON.
    all_rows.extend(data) #Acumula los registros en una sola lista.
    if not data:
      break
    page +=1

  out_file = RAW_DIR / "breweries.json" #Guarda en esa ubicación un archivo con el nombre especificado.
  out_file.write_text(json.dumps(all_rows, indent=2)) # Convierte un objeto Python (dict, list, etc.) en una cadena JSON. data son los datos a obtenidos de la api e indent=2 define el tamaño de las identaciones.
  print(f"Guardadas {len(all_rows)} breweries -> {out_file}") # ?

if __name__ == "__main__" : 
  main()
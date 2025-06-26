import pathlib, json, requests

API_URL = "https://punkapi.online/v3/beers"
RAW_DIR = pathlib.Path(__file__).parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def main():  
  page = 1
  all_data = []
  while True:
    response = requests.get(API_URL, params={"page":page, "per_page":80})
    response.raise_for_status()
    data = response.json()
    if not data:
      break
    all_data.extend(data)
    page += 1

  out_file = RAW_DIR / "beers.json"
  out_file.write_text(json.dumps(all_data, indent=2))
  print(f"{len(data)} Archivos descargados desde {API_URL}")

if __name__ == "__main__" : 
  main()

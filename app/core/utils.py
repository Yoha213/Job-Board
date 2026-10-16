import json

def read_json_file(file_path: str) -> list[dict] | None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"{file_path} Not Found")
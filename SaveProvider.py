import datetime
import os


class SaveProvider:
    def save(object):
        path = f"data/{object.origin_name}/{object.date}.html"
        dir_name = os.path.dirname(path)
        os.makedirs(dir_name, exist_ok=True)
        with open(path, "w") as save_file:
            save_file.write(object.raw_html)

    def loadAll(origin_name):
        if not os.path.isdir(f"data/{origin_name}"):
            print(f"NO SAVE DATA FOR {origin_name}")
            pass

        fileNames = [f for f in os.listdir(f"data/{origin_name}") if os.path.isfile(f"data/{origin_name}/{f}")]
        files = [SaveProvider.open_file(origin_name, f) for f in fileNames]
        return files

    def open_file(origin_name, file_name):
        date_string = os.path.splitext(file_name)[0]
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        with open(f"data/{origin_name}/{file_name}") as file:
            return (date, file.read())
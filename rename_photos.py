import os
import exifread
from datetime import datetime
import click


def rename_photos(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as f:
                tags = exifread.process_file(
                    f, stop_tag='EXIF DateTimeOriginal')
                if 'EXIF DateTimeOriginal' in tags:
                    date_str = str(tags['EXIF DateTimeOriginal'])
                    date_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                    date_str_format = date_obj.strftime('%Y_%m_%d_%H_%M_%S')
                    new_name = date_str_format + os.path.splitext(filename)[1]
                    new_file_path = os.path.join(folder_path, new_name)

                    if os.path.exists(new_file_path):
                        print(
                            f"Fehler: Die Datei '{new_name}' existiert "
                            f"bereits. Die Datei '{filename}' wurde nicht "
                            f"umbenannt."
                        )
                    else:
                        os.rename(file_path, new_file_path)
                        print(f"'{filename}' wurde umbenannt in '{new_name}'.")
                else:
                    print(
                        f"Fehler: Keine EXIF-Daten in '{filename}' gefunden."
                    )


@click.command()
@click.argument('folder_path')
def main(folder_path):
    """
    Dieses Skript benennt Fotos in einem angegebenen Ordner nach dem
    Aufnahmedatum um.
    Der neue Dateiname hat das Format yyyy_mm_dd_hh_mm, und die bestehende
    Dateiendung bleibt erhalten.
    Der Pfad zum Ordner muss als Parameter angegeben werden.
    """
    if not os.path.exists(folder_path):
        print(f"Fehler: Der angegebene Pfad '{folder_path}' existiert nicht.")
        return

    rename_photos(folder_path)


if __name__ == "__main__":
    main()

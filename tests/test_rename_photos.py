import os
import pytest
import rename_photos
from PIL import Image
from PIL import JpegImagePlugin
import piexif


@pytest.fixture
def setup_test_directory(tmp_path):
    """Create a temporary directory with test images."""
    test_dir = tmp_path / "test_photos"
    test_dir.mkdir()

    # Create test images with EXIF data
    image_1_path = test_dir / "image_1.jpg"
    with open(image_1_path, "wb") as f:
        f.write(create_exif_jpeg(datetime_str="2023:08:15 14:30:00"))

    image_2_path = test_dir / "image_2.jpg"
    with open(image_2_path, "wb") as f:
        f.write(create_exif_jpeg(datetime_str="2024:01:10 09:15:00"))

    # Image without EXIF data
    image_3_path = test_dir / "image_3.jpg"
    image_3_path.touch()

    return test_dir


def create_exif_jpeg(datetime_str):
    """Create a JPEG file with EXIF data, containing the given datetime_str."""
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    exif_dict = {
        "Exif": {
            piexif.ExifIFD.DateTimeOriginal: datetime_str
        }
    }
    exif_bytes = piexif.dump(exif_dict)
    output = JpegImagePlugin.JpegImageFile()
    img.save(output, "jpeg", exif=exif_bytes)
    return output.fp.read()


def test_rename_photos_with_valid_exif(setup_test_directory):
    """Test renaming photos with valid EXIF data."""
    folder_path = setup_test_directory
    rename_photos(folder_path)

    assert os.path.exists(folder_path / "2023_08_15_14_30.jpg")
    assert os.path.exists(folder_path / "2024_01_10_09_15.jpg")


def test_rename_photos_without_exif(setup_test_directory):
    """Test renaming photos without EXIF data."""
    folder_path = setup_test_directory
    rename_photos(folder_path)

    # Ensure that the file without EXIF data remains unchanged
    assert os.path.exists(folder_path / "image_3.jpg")


def test_rename_photos_duplicate_name(setup_test_directory, capsys):
    """Test renaming photos with duplicate names."""
    folder_path = setup_test_directory
    # Create a duplicate file with an expected name after renaming
    duplicate_file_path = folder_path / "2023_08_15_14_30.jpg"
    duplicate_file_path.touch()

    rename_photos(folder_path)

    # Ensure duplicate was not overwritten
    assert os.path.exists(duplicate_file_path)
    assert ("Fehler: Die Datei '2023_08_15_14_30.jpg' existiert bereits."
            in capsys.readouterr().out)


if __name__ == "__main__":
    pytest.main(["-v"])

# Rename Photos by Date and Time

This Python script renames photos in a specified folder based on their original date and time of capture. The new filename format is `yyyy_mm_dd_hh_mm`, preserving the existing file extension. This is useful for organizing photos chronologically. If a photo lacks EXIF data, it will not be renamed, and an appropriate message will be displayed. If a file with the intended new name already exists, an error message will be shown.

## Prerequisites

- Python 3.x
- The libraries `exifread` and `click`

## Installation

To set up the environment for running this script, follow these steps:

1. **Create a virtual environment**

   ```sh
   python -m venv venv
   ```

   This will create a virtual environment named `venv`.

2. **Activate the virtual environment**

   - On **Windows**:

     ```sh
     venv\Scripts\activate
     ```

   - On **Linux/macOS**:

     ```sh
     source venv/bin/activate
     ```

3. **Install the required libraries**

   ```sh
   pip install exifread click
   ```

4. **Verify the installation**

   ```sh
   pip list
   ```

   You should see `exifread` and `click` listed.

## Usage

To use the script, run it from the terminal, specifying the path to the folder containing the photos:

```sh
python rename_photos.py path/to/folder
```

Replace `path/to/folder` with the actual path to the folder where your photos are located.

### Notes

- The folder path must be provided as an argument.
- The script only renames files with `.jpg`, `.jpeg`, or `.png` extensions.
- The script will print an error if the provided folder path does not exist.

## Running Tests

If you want to run the tests, you will need additional libraries. Install them using:

```sh
pip install pytest Pillow piexif
```

To run the tests for this script, use the following command:

```sh
pytest
```

Ensure that all the required libraries are installed as mentioned above.

## Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```sh
deactivate
```

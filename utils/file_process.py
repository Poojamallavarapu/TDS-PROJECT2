import os
import zipfile
import tempfile
from pathlib import Path

def unzip_folder(zip_path):
    zip_path = Path(zip_path)

    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    if not zipfile.is_zipfile(zip_path):
        # Create a temporary directory inside /data/tmp_uploads
        base_tmp_dir = Path("/data/tmp_uploads")
        os.makedirs(base_tmp_dir, exist_ok=True)
        temp_dir = Path(tempfile.mkdtemp(dir=base_tmp_dir))
        temp_file_path = temp_dir / zip_path.name
        zip_path.rename(temp_file_path)
        return zip_path,[temp_file_path]

    # Create a temporary directory inside /data/tmp_uploads
    base_tmp_dir = Path("/data/tmp_uploads")
    os.makedirs(base_tmp_dir, exist_ok=True)
    extract_to = Path(tempfile.mkdtemp(dir=base_tmp_dir))

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    # also return the names of the files extracted
    return str(extract_to), zip_ref.namelist()

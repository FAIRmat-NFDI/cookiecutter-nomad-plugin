import os
import tempfile
from {{cookiecutter.module_name}}.example_uploads import example_upload_entry_point


def test_example_upload():
    """Test that all files are correctly created by the example upload.
    Creates a temporary directory and requests the example upload
    to load all files into it.
    """
    with tempfile.TemporaryDirectory() as tmp_upload_directory:
        example_upload_entry_point.load(tmp_upload_directory)
        real_upload_files = []
        for dirpath, _, filenames in os.walk(tmp_upload_directory):
            for filename in filenames:
                real_upload_files.append(
                    os.path.abspath(os.path.join(dirpath, filename))
                )
        assert sorted(real_upload_files) == ['README.md']

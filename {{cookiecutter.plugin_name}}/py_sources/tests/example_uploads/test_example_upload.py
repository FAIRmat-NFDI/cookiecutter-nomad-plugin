import os
import tempfile

from {{cookiecutter.module_name}}.example_uploads import example_upload_entry_point


def test_example_upload():
    """Test that all files are correctly created by the example upload.
    Creates a temporary directory and requests the example upload
    to load all files into it.
    """
    # We set the plugin package name manually in testing: normally it is
    # resolved automatically during the plugin entry point loading
    example_upload_entry_point.plugin_package = '{{cookiecutter.module_name}}'

    with tempfile.TemporaryDirectory() as tmp_upload_directory:
        example_upload_entry_point.load(tmp_upload_directory)
        relative_paths = []
        for dirpath, _, filenames in os.walk(tmp_upload_directory):
            for filename in filenames:

                full_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(full_path, tmp_upload_directory)
                relative_paths.append(relative_path)

        assert sorted(relative_paths) == ['README.md']


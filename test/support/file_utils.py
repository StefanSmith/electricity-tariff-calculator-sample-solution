import os


def absolute_path_to_file(current_file_path, *file_paths):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(current_file_path)), *file_paths))

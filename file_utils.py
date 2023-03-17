import os


def parse_filename(path, keep_extension=False):
    valid_path = path.replace('\\', os.sep)
    basename = os.path.basename(valid_path)

    if keep_extension:
        return basename

    return basename.replace('.mp3', '').replace('.wav', '')

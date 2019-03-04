SUFFIXES = ['KB','MB','GB','TB','PB','EB','ZB','YB']


def approximate_size(size):
    """ convert a file size to human-readable from."""
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024
    for suffix in SUFFIXES:
        size /= SUFFIXES[multiple]
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')
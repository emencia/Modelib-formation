'''Convert file sizes to human-readable form.

Available functions:
approximate_size(size, a_kilobyte_is_1024_bytes)
    takes a file size and returns a human-readable string

Examples:
>>> approximate_size(1024)
'1.0 KiB'
>>> approximate_size(1000, False)
'1.0 KB'

'''

SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        # TODO Display the value in the error message
        raise ValueError('number must be non-negative')

    # This is a conditional expression
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    if size < multiple:
        return f'{size} B'

    for suffix in SUFFIXES[multiple]:
        size = size / multiple # This would be shorter with the /= operator
        if size < multiple:
            return f'{size:.1f} {suffix}'

    raise ValueError('number too large')

# The section won't be executed when importing the module
if __name__ == '__main__':
    sizes = [42, 1000000000000, -5]
    for size in sizes:
        try:
            print(
                f'{size} bytes = {approximate_size(size, False)} or {approximate_size(size)}'
            )
        except ValueError as exc:
            print(exc)

# This will always be executed
print('Hello world')

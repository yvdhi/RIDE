# Automatically generated by 'package.py' script.

VERSION = '0.22.1'
RELEASE = 'final'
TIMESTAMP = '20100326-133208'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE

if __name__ == '__main__':
    import sys
    print get_version(*sys.argv[1:])

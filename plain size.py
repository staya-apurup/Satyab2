def file_size(fname):
    import os
    statinfo =os.stat(fname)
    return statinfo.st_size
print("file size in bytes of a plain file:" ,file_size("abc.txt"))
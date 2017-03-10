"""Helper Python Script for SQL commands and image to hash conversions."""
import glob
import hashlib
import os.path
from os import rename, listdir

# Gonna write a script to automatically add photos to SQL table

# arr = glob.glob('*.jpg')
# album_id_dict = {"sports": 1, "football": 2, "world": 3, "space": 4}
# for name in arr:
#     line = name
#     # extension = os.path.splitext(line)[0]
    
#     first, last = line.split('_')
#     albumid = album_id_dict[first]
#     # print(str(albumid) + ' ' + line)
#     m = hashlib.md5((str(albumid) + line).encode("utf-8"))
#     picid = m.hexdigest()
#     # print picid
#     print line

#     newname = picid + '.jpg'
#     rename(line, newname)
    # print ("INSERT INTO Photo (picid, format) VALUES ('{0}', 'jpg');").format(
        # picid)
    # print ("INSERT INTO Contain (albumid, picid, caption) VALUES ({0}, '{1}','');").format(albumid, picid)
    
m = hashlib.md5((str(1) + 'sports_s1.jpg').encode("utf-8"))
picid = m.hexdigest()
print picid
# from os import rename, listdir

for fname in glob.glob('*.jpg'):
    print(fname)
    line = fname
    extension = line
    first, last = line.split('_')
    albumid = album_id_dict[first]
    m = hashlib.md5((str(albumid) + extension).encode("utf-8"))
    picid = m.hexdigest()
    newname = str(picid) + ".jpg"
    print(newname)
    rename(fname, newname)

# Change filenames to hashed values

# for fname in glob.glob('*.jpg'):
#     print(fname)
#     line = fname
#     extension = line
#     first, last = line.split('_')
#     albumid = album_id_dict[first]
#     m = hashlib.md5((str(albumid) + extension).encode("utf-8"))
#     picid = m.hexdigest()
#     newname = str(picid) + ".jpg"
#     print(newname)
#     rename(fname, newname)
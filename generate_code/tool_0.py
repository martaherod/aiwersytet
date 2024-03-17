from os import walk, path

# root - katalog, w którym jestem; dirs - katalogi w root; files - pliki w root i dirs
for root, dirs, files in walk("code"):
    for file in files:
            print(path.join(root, file))
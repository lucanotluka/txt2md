import os
from pathlib import Path

currDir = [files for files in Path(Path.cwd()).iterdir() if (files.is_file() and os.path.splitext(files)[1]==".txt")]

for myFile in currDir:
    try:
        fileName = os.path.splitext(myFile)[0]
        os.rename(myFile, fileName + '.md')
    except OSError:
        OSError

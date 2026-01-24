import os
import json
from pathlib import Path

# import pathlib as pl

print(os.getenv('HOME'))
print(json.dumps(os.getenv('HOME'), indent=2))

base_path = Path(os.getenv('HOME')) / "documents" / "projects"
print(base_path)

base_path = Path(".") #will point to current working directory
print(base_path.resolve())


# print(pl.Path('.').resolve())

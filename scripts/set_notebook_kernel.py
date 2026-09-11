import nbformat
import sys
from pathlib import Path

nb_path = Path(r"F:\Obsidian\CNC_for Enginners_and_Operators\github_code_repo\CNC_Code_Companion.ipynb")
if not nb_path.exists():
    print("Notebook not found:", nb_path)
    sys.exit(1)

nb = nbformat.read(nb_path, as_version=4)

nb.metadata.setdefault('kernelspec', {})
nb.metadata['kernelspec'].update({
    'name': 'cnc_repo_venv',
    'display_name': 'Python (.venv cnc_repo)',
    'language': 'python'
})

nbformat.write(nb, nb_path)
print('Updated kernelspec in', nb_path)

import nbformat
nb = nbformat.read('CNC_Code_Companion.ipynb', as_version=4)
print('kernelspec ->', nb.metadata.get('kernelspec'))

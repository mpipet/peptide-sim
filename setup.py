from distutils.core import setup
setup(name='peptide-sim',
    version='0.0.1',
    py_modules=['peptide-sim'],
    scripts=['peptideSim', 'pdbToChain'],
    install_requires=['Biopython', 'PeptideBuilder'])
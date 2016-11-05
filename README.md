peptid-sim
=============

peptide-sim is an experiment aiming to reproduce peptide assembly in silico


Methodology
-----------------
use X-ray crystallography pdb files to obtain amino acid peptide sequence 

build back the peptide while trying to mimic the in vitro folding (@TODO)

generate a pdb file to compare with the original


Usage
-----

using pdb file (from www.rcsb.org for example)

Obtain the sequence from pdb file

.. code-block:: bash

  $ pdbToChain 1qbf.pdb


Generate the simulated peptide pdb file 

.. code-block:: bash

  $ pdbToChain ../pdbs/1qbf.pdb|peptideSim > simulated_1qbf.pdb


Use your favorite pdb viewer (rasmol for example)

.. code-block:: bash

  $ rasmol simulated_1qbf.pdb 

Installation
------------

.. code-block:: bash

  $ python setup.py install




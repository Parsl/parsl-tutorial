.. image:: https://mybinder.org/badge.svg :target: https://mybinder.org/v2/gh/Parsl/parsl-tutorial/master

Parsl Tutorials
===============

Parsl is a parallel scripting library for Python that allows users to develop and execute dataflow scripts on parallel and distributed resources.

Parsl runs programs concurrently as soon as their inputs are available, reducing the need for complex parallel programming. Parsl expresses dataflow in a portable fashion: the same script can run on multicore computers, clusters, clouds, grids, and supercomputers.

This repository inlcudes three tutorials: 
 - parsl-introduction.ipynb: a quickstart guide to using Parsl
 - parsl-workflows.ipynb: example workflow patterns expressed in Parsl
 - parsl-advanced-features.ipynb: examples of various Parsl features such as multi-site, elasticity, and fault tolerance

The tutorial repository includes everything needed to run these nodebooks. It includes sample applications ``simulate`` and ``stats`` (mock "science" applications) as well as a basic MPI program. It also includes configuration files for several compute resources. 


Running with Binder
-------------------

The easiest way to run this tutorial is via Binder. Using Binder you can run the tutorial notebooks in your browser without installing any code locally.

`Start Binder <https://mybinder.org/v2/gh/Parsl/parsl-tutorial/master>`_.


Running locally
---------------

To run the tutorial locally, ensure that Python (3.5+) and Parsl is installed.

To install Parsl:: 

  $ pip3 install parsl


To install Parsl from source, see the `documentation <http://parsl.readthedocs.io/en/latest/quickstart.html>`_.

Finally, set up the Parsl tutorial::

    $ git clone https://github.com/parsl/parsl-tutorial.git
 


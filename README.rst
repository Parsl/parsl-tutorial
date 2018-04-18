Parsl is a powerful library for executing dataflow scripts in Python.

Parsl runs programs concurrently as soon as their inputs are available, reducing the need for complex parallel programming. Parsl expresses dataflow in a portable fashion: the same script can run on multicore computers, clusters, clouds, grids, and supercomputers.

In this tutorial, you will be able to first try a few Parsl examples (examples 1-4) on your local machine, to get a sense of the language. Then, in examples 5-7 you will run similar workflows on any resource you may have access to, such as clouds (Amazon Web Services), Cray HPC systems, clusters etc, and see how more complex workflows can be expressed with Parsl scripts.

To run the tutorial, ensure that Python (3.5+) and Parsl is installed.

To install Parsl:: 

  $ pip3 install parsl


To install Parsl from source, see the `documentation <http://parsl.readthedocs.io/en/latest/quickstart.html>`_.

Finally, set up the Parsl tutorial::

    $ git clone https://github.com/parsl/parsl-tutorial.git
 

The tutorial repository includes sample applications ``simulate`` and ``stats`` (mock "science" applications) as well as a basic MPI program. It also includes configuration files for several compute resources. 

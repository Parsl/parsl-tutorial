Parsl is a simple scripting library for executing dataflow-based dependency in Python.


Parsl runs programs concurrently as soon as their inputs are available, reducing the need for complex parallel programming. Parsl expresses workflow in a portable fashion: The same script can run on multicore computers, clusters, clouds, grids, and supercomputers.

In this tutorial, you will be able to first try a few Parsl examples (examples 1-4) on your local machine, to get a sense of the language. Then, in examples 5-7 you will run similar workflows on any resource you may have access to, such as clouds (Amazon Web Services), Cray HPC systems, clusters etc, and see how more complex workflows can be expressed with Parsl scripts.

To run the tutorial, ensure that Python (3.5+) and Parsl 0.3 is installed on the machine you would be using to run the tutorial on.

To install Parsl: 

$ pip3 intsall parsl

To install Parsl from source:
  1. Download Parsl::

    $ git clone https://github.com/Parsl/parsl.git parsl

  2. Install::

    $ cd parsl
    
    $ python3 setup.py install


Setup the Parsl tutorial::

    $ git clone https://github.com/parsl/parsl-tutorial.git
 

The tutorial repository includes sample applications ``simulate`` and ``stats`` (mock "science" applications) as well as a basic MPI program. It also includes configuration files for several resources. 

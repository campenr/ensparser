multiplate 0.1a1
===============

Bugs and issue tracking
-----------------------

This script has not been tested against all output file permutations and
as such may incorrectly parse csv files output from certain protocols. Bug
reports should be submitted via the github issue tracker.

Description
-----------

This package was built for python 3 and as such may not be backwards compatible
with python 2.

This package contains modules for parsing output files from multiplate readers.
Currently only csv output files from the Perkin Elmer 2300 Multilabel plate reader
are supported. For details on the specific implementation of outfile file parsing
consult the relevant source file.

Plate data sets from output files are converted to pandas DataFrame objects with
the following structure:

+-------+-------+-------+-------+-------+-------+-------+-------+
|       |     1 |     2 |     3 |     4 |     5 |     6 |     7 |
+-------+-------+-------+-------+-------+-------+-------+-------+
|0      |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|A      |19106  | 18954 |  23140| 21745 |  24585|  22294| 25033 |
+-------+-------+-------+-------+-------+-------+-------+-------+
|B      |18427  | 274628| 285552|201486 | 245432| 237888| 232065|
+-------+-------+-------+-------+-------+-------+-------+-------+
|C      |18618  |228774 |  95715|116193 | 254504| 161491| 190138|
+-------+-------+-------+-------+-------+-------+-------+-------+
|D      |19658  | 230940|143189 | 137232| 167545| 85874 |  76320|
+-------+-------+-------+-------+-------+-------+-------+-------+

Usage
-----

The ``parse_csv(file)`` function takes a csv file path as a string as it's only
argument. Handling of opening of the file is done within the function. To iterate
over a list of files, parse the data sets from those files, and save each data set
to a separate file (using pandas to_csv) for example: ::

  from ensparser import ensparser
  for file in list_of_files:
      data_sets = ensparser.parse_csv(file)
      for index, data_set in enumerate(data_sets):
           with open("data_set_{number}.format(number=index), "w") as out_handle:
                data_set.to_csv(out_handle)

Installation
------------

Download source package and run ``setup.py install``

License
-------

This software is released under the Modified BSD license. See
LICENSE.txt for the full license.
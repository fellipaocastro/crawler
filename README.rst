Crawler
=======

Crawler that looks for the following store's products and saves their name,
title and URL in a CSV file without duplicated entries.

`Época Cosméticos Perfumaria <http://www.epocacosmeticos.com.br>`_

Requirements
------------

.. code-block:: bash

   Python 2.7.8
   pip 1.5.6

Setup
-----

.. code-block:: bash

   $ pip install -r requirements.txt

Usage
-----

.. code-block:: bash

   $ ./run.sh

Test
----

.. code-block:: bash

   $ nosetests --with-spec --spec-color test.py

Source code check
-----------------

.. code-block:: bash

   $ flake8 . --verbose

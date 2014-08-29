Crawler
=======

This is a crawler that scrapes products from
`Época Cosméticos Perfumaria <http://www.epocacosmeticos.com.br>`_ store and
saves their name, title and URL in a CSV file without duplicated entries.

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

   $ ./manage.sh run

Test
----

.. code-block:: bash

   $ nosetests --with-spec --spec-color test.py

Source code check
-----------------

.. code-block:: bash

   $ ./manage.sh check

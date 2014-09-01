Crawler
=======

This is a crawler that scrapes products from
`Época Cosméticos Perfumaria <http://www.epocacosmeticos.com.br>`_ store and
saves their name, title and URL in a CSV file without duplicated entries.

The items scraped by this project are products, and the item is defined in the class:

    crawler.items.EcpItem

This project contains one spider called ``ecp`` that you can see by running:

.. code-block:: bash

    $ scrapy list

See the source code for more details.

Requirements
------------

- Python 2.7.8
- pip 1.5.6

Setup
-----

.. code-block:: bash

    $ pip install -r requirements.txt

Usage
-----

.. code-block:: bash

    $ ./manage.sh run

Output
------

    /tmp/ecp.csv

.. code-block:: bash

    $ ./manage.sh read

Log
---

    /tmp/crawler-YYYY-MM-DD.log (e.g. /tmp/crawler-2014-09-01.log)

.. code-block:: bash

    $ ./manage.sh log

Test
----

.. code-block:: bash

    $ ./manage.sh test

Source code check
-----------------

.. code-block:: bash

    $ ./manage.sh check

Crawler
=======

Crawler that looks for the following store's products and saves their name,
title and URL in a CSV file without duplicated entries.

|store_link|

.. |location_link| raw:: html

      <a href="http://www.epocacosmeticos.com.br" target="_blank">Época Cosméticos Perfumaria</a>

Requirements
------------

.. code-block:: bash

    Python 2.7.8
    pip 1.5.6

Setup
-----

.. code-block:: bash

    $ pip install -r requirements.txt

Run
---

.. code-block:: bash

    $ python crawler.py

Test
----

.. code-block:: bash

    $ nosetests --with-spec --spec-color test.py

Source code check
-----------------

.. code-block:: bash

    $ flake8 . --verbose

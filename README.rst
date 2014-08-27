Crawler
=======

Crawler that looks for Época Cosméticos' products and saves their name, title
and URL in a CSV file without duplicated entries.

URL: `<http://www.epocacosmeticos.com.br>`_

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

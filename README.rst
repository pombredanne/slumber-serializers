=============
slumber-extra
=============

A set of Slumber extras

.. image:: https://codeclimate.com/github/tomi77/slumber-extra/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/slumber-extra
   :alt: Code Climate
.. image:: https://travis-ci.org/tomi77/slumber-extra.svg?branch=master
   :target: https://travis-ci.org/tomi77/slumber-extra
.. image:: https://coveralls.io/repos/github/tomi77/slumber-extra/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/slumber-extra?branch=master

Installation
============

Install package via ``pip``
::

    pip install slumber-extra

Usage
=====

::

    import slumber
    import slumber.serialize
    from slumber_serializers import CsvSerializer


    api = slumber.API('/api/v1/', serializer=slumber.serialize.Serializer(default='csv',
                                                                          serializers=[CsvSerializer()]),
                      format='csv')
    api.test(format='csv').get()

CSR AND KEY GNERATOR FOR SSL
============================

I created this script to make it easier to generate the SSL certificates for
the 5 e-commerce websites that I am responsible for.

Requirements
------------

* [pkiutils](https://github.com/jandd/python-pkiutils)

Usage
-----

```shell
python genssl.py --country GB --state Birmingham --locality Birmingham --organisation "Your Company" www.example.com
```

GENSSL
======

Script was created to make it easier to generate CSR when setting up new SSL
certificate for our servers.

Requirements
------------

* [pkiutils](https://github.com/jandd/python-pkiutils) - install via ```pip install pkiutils```
* openssl

Example Usage
-------------

```shell
$ python genssl.py --country GB --state Birmingham --locality Birmingham --organisation "Company Ltd" www.example.co.uk
```

To Do
-----
1. Create basic TKinter interface for script.
2. Create basic Flask app similar to https://www.digicert.com/easy-csr/openssl.htm

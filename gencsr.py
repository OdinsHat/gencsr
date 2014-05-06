#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script is a very light wrapper for pkitils. It basically implements a
single command for generating a CSR/KEY file for SSL creation.

Copyright (c) 2013-2014, Doug Bromley <doug@tintophat.com>
License: BSD (see LICENSE for details)
"""

__author__ = "Doug Bromley"
__email__ = "doug@tintophat.com"
__license__ = "BSD"

import pkiutils
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Generate CSR and key for SSL certificate")

    parser.add_argument("cn", help="The full domain name e.g. www.example.com")
    parser.add_argument("-c", "--country", action="store", help="The 2-character country code")
    parser.add_argument("-s", "--state", action="store", help="The State, County or Province")
    parser.add_argument("-l", "--locality", action="store", help="The locality (e.g. City or town)")
    parser.add_argument("-o", "--organisation", action="store", help="The company or organisation")
    parser.add_argument("-d", "--dept", action="store", default="Web Security", help="Department of the company")
    parser.add_argument("-p", "--path", action="store", default="/root/", help="The path to create the keyfile and csr file")

    args = parser.parse_args()

    if not args.state or not args.locality or not args.country or not args.organisation:
        parser.print_help()
        sys.exit(-1)

    dname = ("/C=%s/ST=%s/L=%s/O=%s/OU=%s/CN=%s" % (
        args.country,
        args.state,
        args.locality,
        args.organisation,
        args.dept,
        args.cn
    ))

    key = pkiutils.create_rsa_key(
        2048,
        keyfile="%s%s.key" % (args.path, args.cn)
    )
    pkiutils.create_csr(
        key,
        dn=dname,
        csrfilename=("%s%s.csr" % (args.path, args.cn)))

if __name__ == "__main__":
    main()
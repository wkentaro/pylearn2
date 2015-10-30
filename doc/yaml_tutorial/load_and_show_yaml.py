#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from pylearn2.config import yaml_parse


parser = argparse.ArgumentParser()
parser.add_argument('yaml_file')
args = parser.parse_args()

with open(args.yaml_file) as f:
    model = yaml_parse.load(f)
    print model
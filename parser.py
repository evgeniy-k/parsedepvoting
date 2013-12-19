#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import gettext

gettext.bindtextdomain('depvotingparser', localedir='locale')
gettext.textdomain('depvotingparser')
_ = gettext.gettext

if len(sys.argv) < 2:
  print _('No input file with report form! Usage: ./parser.py [filename]')
  exit

print _('Opening file: %s' % sys.argv[1])
try:
  f = open(sys.argv[1], 'r')
except IOError:
  print >> sys.stderr, _('Error open file: %s' % sys.argv[1])
else:
  f.close()  

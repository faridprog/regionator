#!/usr/bin/env python

"""
Copyright (C) 2007 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
$URL$
$Revision$
$Date$
"""

import os
import sys
import kml.modelator

if len(sys.argv) != 4:
  print 'usage: %s modeldir rootkml outputdir' % sys.argv[0]
  sys.exit(1)

modeldir = sys.argv[1]
rootkml = sys.argv[2]
outputdir = sys.argv[3]

try:
  os.makedirs(outputdir)
except:
  print '%s exists' % outputdir
  sys.exit(1)
  

kml.modelator.BasicModelRegionator(modeldir, rootkml, outputdir)

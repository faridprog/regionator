#!/usr/bin/python

"""
Copyright (C) 2006 Google Inc.

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

import unittest
import os
import kml.region
import kml.regionhandler
import kml.regionator
import kml.genkml
import kml.kmlparse


class NullRegionatorTestCase(unittest.TestCase):
  def runTest(self):
    class NullRegionHandler(kml.regionhandler.RegionHandler):
      """inherits all RegionHandler methods"""

    nullrtor = kml.regionator.Regionator()
    nullrtor.SetRegionHandler(NullRegionHandler())
    region = kml.region.Region(20,10,40,30,'0')
    nullrtor.Regionate(region)
    assert nullrtor.MaxDepth() == 0, 'Null rtor MaxDepth() bad'
    assert nullrtor.RegionCount() == 0, 'Null rtor RegionCount() bad'
    assert len(nullrtor.QidList()) == 0, 'Null rtor QidList() bad'
    nullroot = nullrtor.RootRegion()
    assert nullroot.NSEW() == region.NSEW(), 'Null rtor RootRegion() bad'


class SimpleRegionatorTestCase(unittest.TestCase):
  def runTest(self):

    class SimpleRegionHandler(kml.regionhandler.RegionHandler):

      def Start(self, region):
        # Recurse 2 levels
        if region.Depth() > 2:
          return [False,False]
        return [True,True]

    l2rtor = kml.regionator.Regionator()
    l2rtor.SetRegionHandler(SimpleRegionHandler())
    region = kml.region.Region(30,10,40,20,'0')
    l2rtor.Regionate(region)
    assert l2rtor.MaxDepth() == 2, 'Simple rtor MaxDepth() bad'
    assert l2rtor.RegionCount() == (1+4), 'Simple rtor RegionCount() bad'
    l2qidlist = l2rtor.QidList()
    assert len(l2qidlist) == (1+4), 'Simple rtor QidList() bad'
    assert l2qidlist[0] == '0', 'Simple rtor qid 0 bad'
    assert l2qidlist[1] == '00', 'Simple rtor qid 00 bad'
    assert l2qidlist[2] == '01', 'Simple rtor qid 01 bad'
    assert l2qidlist[3] == '02', 'Simple rtor qid 02 bad'
    assert l2qidlist[4] == '03', 'Simple rtor qid 03 bad'
    l2root = l2rtor.RootRegion()
    assert l2root.NSEW() == region.NSEW(), 'Simple rtor RootRegion() bad'


class SmallRegionatorTestCase(unittest.TestCase):
  def runTest(self):

    class SmallRegionHandler(kml.regionhandler.RegionHandler):

      def __init__(self, dir):
        self.__dir = dir

      def Start(self, region):
        # Recurse 4 levels
        if region.Depth() > 4:
          return [False,False]
        return [True,True]

      def Data(self, region):
        (lon,lat) = region.MidPoint()
        return kml.genkml.PlacemarkPoint(lon,lat,region.Qid())

      def Kml(self, region, kmlfile, kml):
        pathname = os.path.join(self.__dir, kmlfile)
        f = open(pathname, 'w')
        f.write(kml)
        f.close()

    # Create a Region NetworkLink hierarchy in the test directory
    smallrtor = kml.regionator.Regionator()
    testdir = 'smallrtortestdir'
    os.makedirs(testdir)
    smallrtor.SetRegionHandler(SmallRegionHandler(testdir))
    root = kml.region.Region(90,-90,180,-180,'0')
    smallrtor.Regionate(root)

    # Verify state of rtor 
    assert smallrtor.MaxDepth() == 4, 'Small rtor MaxDepth() bad'
    want_count = (1+4+16+64)
    assert smallrtor.RegionCount() == want_count, 'Small rtor RegionCount() bad'
    qidlist = smallrtor.QidList()
    assert len(qidlist) == want_count, 'Small rtor QidList() bad'

    # Verify state of generated KML files
    kp = kml.kmlparse.KMLParse(os.path.join(testdir, '1.kml'))
    # First LatLonAltBox is Region at top of file
    llab = kp.ExtractLatLonAltBox()
    assert llab.Get_NSEW() == root.NSEWstring(), 'Small rtor 1.kml bad'

    kp = kml.kmlparse.KMLParse(os.path.join(testdir, '85.kml'))
    llab = kp.ExtractLatLonAltBox()
    want_nsew = ('-67.5', '-90', '180', '135.0')
    assert llab.Get_NSEW() == want_nsew, 'Small rtor 85.kml bad'


def suite():
  suite = unittest.TestSuite()
  suite.addTest(NullRegionatorTestCase())
  suite.addTest(SimpleRegionatorTestCase())
  suite.addTest(SmallRegionatorTestCase())
  return suite


print 'test Regionator ... begin'
runner = unittest.TextTestRunner()
runner.run(suite())
print 'test Regionator ... end'
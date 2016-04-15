# Introduction #

This describes the classes at the core of the Regionator which are as follows:

  * kml.regionator.Regionator
  * kml.regionhandler.RegionHandler
  * kml.region.Region

# Overview #

Create a Region.  Create a RegionHandler.  Create a Regionator which walks the hierarchy calling your RegionHandler for each child region.  A child region is one of 4 quadrants of a parent region.  Thus the hierarchy is a 4-way tree.

The Region represents the bounding box of the objects to "regionate", for example a large number of Placemarks.

You define one or more methods in your RegionHandler-derived class.  A basic RegionHandler class implements Start() and Data().  In Start() the Regionator is asking you if there is data for this region and below.  If your Start() returns True for data at this region your Data() method will be called for you to return a KML Feature representing the KML you want loaded and displayed for this region.  A Feature is anything from a simple Placemark or GroundOverlay to a Folder containing many Placemarks or any number of other Features, etc.  The Regionator takes care of creating the NetworkLink portion of the KML for that region and a file per region is saved to the directory specified in SetOutputDir().

## Example: box hierarchy ##

See tests/boxes.py for a simple RegionHandler which builds a hierarchy of LineString boxes.

BoxRegionHandler() is derived from kml.regionhandler.RegionHandler().  The Start(), Data() and PixelLod() methods are implemented as follows.  Start() simply indicates that a box is to be drawn in this region and it bases this decision on the depth of hierarchy which in turn is an argument to the script.  Data() is a Placemark holding a LineString representing the outline of the bounding box of that Region.  PixelLod() overrides the default min and max lod values.

myregionator is an instance of kml.regionator.Regionator() which writes the KML to the directory passed to SetOutputDir() and which descends down a hierarchy based on the n,s,e,w arguments to the program.

myregionator.Regionate() runs the overall regionating process.







This project includes a collection of Python classes
and scripts which can be used to generate and verify Region-based KML.

## Scripts ##

Here are some useful scripts:

  * checkcsvlinks.py - check HTML link targets in a CSV file
  * checklinks.py - walk a RbNL hierarchy
  * checkregions.py - check Region elements in an RbNL hiearchy
  * csvregionator.py - CSV point data in, RbNL out
  * getkml.py - get the doc.kml in KMZ file or URL
  * kmlsuperoverlay.py - GTiff in, SuperOverlay out
  * mkregionboxes.py - create boxes for the Regions in an RbNL hierarchy
  * placemarks.py - KML Placemarks in, RbNL out

## Classes ##

Here are some useful modules.  Use pydoc on each module for more info:

  * kml.checklinks - module for checking KML ahd HTML links
  * kml.checkregions - module for checking KML Regions
  * kml.cvsregionator - CSV regionator mainline
  * kml.featureset - container for a set of features
  * kml.genkml - convenience functions for generating KML
  * kml.genxml - KML types (Placemark, Folder, NetworkLink, etc)
  * kml.href - KML href support and fetch
  * kml.kmlregionator - KML regionator main module
  * kml.kmz - KMZ archive support
  * kml.model - KML Model support
  * kml.photooverlay - KML PhotoOverlay support
  * kml.region - KML Region support
  * kml.regionator - core "regionator" algorithm
  * kml.regionhandler - base class for building specific regionators
  * kml.superoverlay - SuperOverlay main module
  * kml.walk - KML RbNL walker
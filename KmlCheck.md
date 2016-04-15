# Introduction #

This describes the scripts and classes that check various aspects of KML NetworkLink hierarchies:

  * checklinks.py
  * checkregions.py

## checklinks.py ##

```
% checklinks.py [-k] [-h] [-a] [-r] [-v] [-s] [-c] [-e encoding] -u url.kml
   -k: check KML hrefs
   -h: check HTML hrefs
   -a: check absolute URLs
   -r: check relative URLs
   -c: compute checksum
   -v: verbose
   -s: print summary only
   -e encoding: override xml encoding
   -u url.kml: KML file or hierarchy to check
%
```

With no arguments checklinks.py walks the KML NetworkLink hiearchy
rooted at url.kml.  url.kml can be a local file or a network URL.
All NetworkLink children are fetched irrespective of refresh mode.

The -k specifies to follow all KML hrefs: Overlay's Icon and Model's Link.

The -h specifies to follow hrefs within embedded HTML.

The -r specifies to follow relative links for either -k or -h.

The -a specifies to follow absolute links for either -k or -h.

With a -v one line of output is generated per checked item.
The item being checked is indicated by the first letter of each line:

```
P    parent link
C    child link (raw <href>)
U    full URL of child (relative href w.r.t. parent)
ERR failed-link parent-url
X    summary
```

With -s a summary is printed:

```
% checklinks.py -rksu ch-basic-root.kml 
X   1798 nodes
X   1797 kml links
X   1797 relative links
X   0 hostname links
X   0 empty links
X   5251 max
X   ch-basic-dir/450.kml
X   576 min
X   ch-basic-dir/15.kml
X   4417193 total bytes
X   1797 files
X   2458 average bytes/file
X   293.3M average bps
X   12 seconds overall
X   2.7M overall bps
X   0 errors
%
```

With -c a checksum of all data fetched is computed:

```
% checklinks.py -rkscu ch-basic-root.kml 
X   1798 nodes
X   1797 kml links
X   1797 relative links
X   0 hostname links
X   0 empty links
X   5251 max
X   ch-basic-dir/450.kml
X   576 min
X   ch-basic-dir/15.kml
X   4417193 total bytes
X   1797 files
X   2458 average bytes/file
X   296.1M average bps
X   12 seconds overall
X   2.7M overall bps
X   0 errors
X   9b1bf617e0a7621b403e074fd2a8fdd9 checksum
%
```

## checkregions.py ##

```
% checkregions.py [-v] url.kml
   -v: verbose
%
```

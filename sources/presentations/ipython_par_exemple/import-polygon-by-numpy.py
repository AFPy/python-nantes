#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From http://py2gis.blogspot.com/2010/10/import-polygon-by-numpy.html
from osgeo import ogr
from matplotlib import pyplot
from numpy import asarray
from shapely.wkb import loads

#plot polygon only
source = ogr.Open("voronoi_stations.shp")
layer = source.GetLayerByName("voronoi_stations")
#print layer
fig = pyplot.figure(1, figsize=(5,4), dpi=150)
ax = fig.add_subplot(111)
def plot_poly(g):
    a = asarray(g.exterior)
    pyplot.plot(a[:,0], a[:,1])
while 1:
    feature = layer.GetNextFeature()
    if not feature:
        break
    geom = loads(feature.GetGeometryRef().ExportToWkb())
    #print geom
    if geom.geom_type == 'MultiPolygon':
        for g in geom:
            plot_poly(g)
    if geom.geom_type == 'Polygon':
        plot_poly(geom)
pyplot.show()


#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#from variables_config import * # Contains shared variables (See http://docs.python.org/faq/programming.html#how-do-i-share-global-variables-across-modules)

# get extent from shp (for mapnik)
from ogr_extent import *

# Retrieve extent and projection using gdal
shp_extent , proj4 = extent_and_proj('departement.shp', sourcetype = 'ESRI Shapefile')


import cairo
from mapnik import Style, Rule, Color, Filter, LineSymbolizer, PolygonSymbolizer, TextSymbolizer, label_placement, Shapefile, SQLite, Layer, Map, render, Shapefile, Expression, save_map

map_output = 'france'
m = Map(300, 300, proj4)

m.background = Color('steelblue')

t = TextSymbolizer(Expression('[CODE_DEPT]'), 'DejaVu Sans Book', 8, Color('black'))

f = Expression("[CODE_DEPT]<>'75' and [CODE_DEPT]<>'92' and [CODE_DEPT]<>'93' and [CODE_DEPT]<>'94'")
t.allow_overlap = 1
t.label_placement = label_placement.POINT_PLACEMENT
s1 = Style()
r1 = Rule()
r1.symbols.append(t)
r1.filter = f
s1.rules.append(r1)
m.append_style('Text', s1)

s = Style()
r = Rule()
r.symbols.append(PolygonSymbolizer(Color('#f2eff9')))
r.symbols.append(LineSymbolizer(Color('rgb(50%,50%,50%)'), 0.1))
s.rules.append(r)
m.append_style('My Style', s)

lyr = Layer('france', proj4)
import os

shp = Shapefile(base='.',file='departement') 

lyr.datasource = shp
#lyr.datasource = SQLite(base=os.getcwd(), file = sqlitedatabase, table = tablename, geometry_field = 'Geometry', key_field = 'ID_GEOFLA', extent = shp_extent, wkb_format = 'spatialite')

lyr.styles.append('My Style')
lyr.styles.append('Text')

m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())

file_formats = {'svg': cairo.SVGSurface,
                       }

for type_format in file_formats:
    print '// --  Rendering %s -----------------------------' % type_format
    file_open = open('%s.%s' % (map_output, type_format), 'w')
    surface = file_formats[type_format](file_open.name, m.width, m.height)
    render(m, surface)
    save_map(m,"tmp_map.xml")
    surface.finish()


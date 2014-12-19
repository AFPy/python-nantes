# import modules
from osgeo import ogr
import os, sys

def extent_and_proj(file = "france.sqlite", sourcetype = 'SQLite', table = "departements"):
    # get the shapefile driver
    driver = ogr.GetDriverByName(sourcetype)

    # open the data source
    datasource = driver.Open(file, 0)
    if datasource is None:
      print 'Could not open file'
      sys.exit(1)

    # get the data layer
    if sourcetype == 'SQLite':
        layer = datasource.GetLayerByName(table)
    else:
        layer = datasource.GetLayer()

    # get Extent
    layerExtent = layer.GetExtent()
    # get spatial ref
    spatialReference = layer.GetSpatialRef()
    #strExtent = ",".join([str(coords) for coords in layerExtent])
    # Specific order for mapnik
    strExtent = str(layerExtent[0]) + "," + str(layerExtent[2]) + "," + str(layerExtent[1]) + "," + str(layerExtent[3])
    return strExtent, spatialReference.ExportToProj4().strip()



# In mapnik
# '99226.000000,6049647.000000,1242375.000000,7110524.000000'

# Current OGR return
# 99226.0, 1242375.0, 6049647.0, 7110524.0


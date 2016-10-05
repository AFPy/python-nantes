#!/usr/bin/env python
# encoding: utf-8

"""
Plot_shapely.py
Martin Laloux 2010
"""
import pylab
from shapely.wkt import loads
from descartes.patch import PolygonPatch
class Plot_shapely(object):
    """dessin de géométries Shapely avec matplotlib - pylab"""
     
    def __init__(self,obj,ax, coul=None, alph=1):
        """
        Paramètres
        ----------------------------------------------------------------
        ax de pylab, obj = objet géometrique, coul = couleur matplotlib, alph = transparence
         
        Exemple
        --------------------------------------------------------------------
        >>> from shapely.wkt import loads
        >>> ax = pylab.gca()
        >>> ligne = loads('LINESTRING (3 1, 4 4, 5 5, 5 6)')
        >>> a = Plot_shapely(ligne,ax,'r', 0.5)
        >>> a.plot
        ou directement
        >>> Plot_shapely(ligne,ax,'#FFEC00'').plot
        >>> pylab.show()
        """
        self.obj = obj
        self.type = obj.geom_type
        self.ax = ax
        self.coul= coul
        self.alph=alph
     
    def plot_coords(self):
        """points"""
        x, y = self.obj.xy
        self.ax.plot(x, y, 'o', color=self.coul)
     
    def plot_ligne(self):
        """lignes"""
        x, y = self.obj.xy
        self.ax.plot(x, y, color=self.coul, alpha=self.alph, linewidth=3)
     
    def plot_polygone(self):
        """polygones"""
        patch = PolygonPatch(self.obj, facecolor=self.coul,edgecolor=self.coul, alpha=self.alph)
        self.ax.add_patch(patch)
     
    def plot_multi(self):
        """multipoints, multilignes,multipolygones + GeometryCollection"""
        for elem in self.obj:
            Plot_shapely(elem, self.ax, self.coul,self.alph).plot
     
     
    @property
    def plot(self):
        """dessine en fonction du type géometrique"""
        if self.type == 'Point':
            self.plot_coords()
        elif self.type == 'Polygon':
            self.plot_polygone()
        elif self.type == 'LineString':
            self.plot_ligne()
        elif "Multi" in self.type:
            """ex. MultiPolygon"""
            self.plot_multi()
        elif self.type == 'GeometryCollection':
            self.plot_multi()
        elif self.type == 'LinearRing':
            self.plot_line()
        else:
            raise ValueError("inconnu au bataillon: %s" % self.type)
 
if __name__ == '__main__':
import doctest
doctest.testmod()


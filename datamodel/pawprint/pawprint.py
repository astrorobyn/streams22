from matplotlib.path import Path as mpl_path

class pawprintClass(dict):
    '''Dictionary class to store a "pawprint": polygons in multiple observational spaces that define an initial selection used for stream track modeling, membership calculation / density modeling, or background modeling.'''

    def __init__(self):
        self.skyprint = {} #polygon(s) in stream coordinates phi1, phi2
        self.streamspec = {} #rotation matrix to transform from ??? to phi1/phi2
        self.cmdprint = {} #polygon(s) in cmd space
        self.cmdspec = {} #some kind of specification for which colors and mags?
        self.pmprint = {} #polygon(s) in proper-motion space
        self.pmspec = {} #some way to specify which PM coordinates the polygons are functions of
        
    def _inside_poly(data, vertices):
        '''This function takes a list of points (data) and returns a boolean mask that is True for all points inside the polygon defined by vertices'''
        return mpl_path(vertices).contains_points(data)

    def in_pawprint(self, data):
        '''will take in some data and return masks for stuff in the pawprint (basically by successively applying _inside_poly'''

    
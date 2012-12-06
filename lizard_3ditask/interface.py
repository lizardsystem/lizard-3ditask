# Prototype interface for 3di library.

class ThreeDi(object):

    ##### Essentials #####
    def __init__(self, mdu_filename):
        """Initialize a new 3Di calculation instance

        read mdu, prepare model, build quad trees, etc.
        """
        pass

    def step(self):
        """Calculate a step (should normally return in
        about 1 second)"""
        pass

    def waterlevels(self):
        """
        Get waterlevels for current time step for each flow element.

        Netcdf?
        """
        pass

    def flow_elements(self):
        """return the coordinates for each flow element"""
        pass

    ##### Updates (later) #####
    def update_bathymetry(self, update):
        """
        Update bathymetry
        """
        pass

    def set_rainfall(self, update):
        """
        Apply rainfall to current timestep.
        """
        pass

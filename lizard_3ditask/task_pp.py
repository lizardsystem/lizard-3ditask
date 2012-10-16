# Running this code in linux, no errors with combination gdal and
# netCDF4

import os

#from read_3di import *
from nc import Data

from netCDF4 import Dataset


def process_3di_nc(filename):
    """Process result netcdf file"""

    #from netCDF4 import Dataset
    rootgrp = Dataset(filename, 'r', format='NETCDF4')
    # for variable_name, variable in rootgrp.variables.items():
    #     print variable_name, variable

    # Depth
    dep = rootgrp.variables['dep']  # timestep, elem
    flow_elem_contour_x = rootgrp.variables['FlowElemContour_x']  # elem, value
    flow_elem_contour_y = rootgrp.variables['FlowElemContour_y']

    #import pdb; pdb.set_trace()

    num_timesteps, num_elements = dep.shape

    # Safety checks
    assert flow_elem_contour_x.shape == flow_elem_contour_y.shape
    assert num_elements == flow_elem_contour_x.shape[0]

    #
    for timestep in range(num_timesteps):
        print('Working on timestep %d...' % timestep)
        for elem in range(num_elements):
            dep[timestep, elem]
            flow_elem_contour_x[elem]
            flow_elem_contour_y[elem]

    rootgrp.close()


def post_process_3di(full_path):
    print 'post processing %s...' % full_path
    #nc_data = Data(full_path)
    process_3di_nc(full_path)

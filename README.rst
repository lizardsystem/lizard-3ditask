lizard-3ditask
==========================================

An app for running 3Di scenarios. It currently partly runs under
Windows.

Windows part:
1) Prepare scenario dir by copying files
2) Run the scenario with 3Di

Linux part:
3) Read the resulting netCDF file and make images / .asc of it.

Doing 3) with linux, because there were problems with the combination
of use of netCDF4 and GDAL under windows.


Prerequisites
-------------

Windows
- Windows, because of 3Di executable.
- 3Di 0.1.1.224:225M or newer
- Psycopg2
- Setuptools
- Numpy 1.6.2 (tested)
- Tested with Python 2.7
- GDAL (see below)


Linux
- sudo pip install netcdf4

Development installation
------------------------

Checkout, install the prerequisites and run:

    > python bootstrap.py
    > bin\buildout


Installation on windows machine (copied from radar)
===================================================

More info than needed, but it can become useful later.

Install using windows 32bit installers:
    matplotlib
    python27
    msysgit
    scipy
    numpy
    h5py
    PIL (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil) (May be after
    different timestamp implementation, not necessary anymore)
Install using OSGeo4W installer, in libs check only:
    gdal-python
The dependencies will be selected automatically. It will
install numpy along the way, which we don't want, so in
C:\OSGeo4W\apps\python27\lib\site-packages delete the numpy directory.

add to path:
    C:\python27;C:\OSGeo4W\bin;

add the following system variables:
    pythonpath=C:\OSGeo4W\apps\python27\lib\site-packages;
    gdal_data=C:\OSGeo4W\share\epsg_csv
    proj_lib=C:\OSGeo4W\share\proj

add id_rsa for pulling to .ssh directory
ask Reinout to add the repo to the NenS pull only team.

in git bash, clone the repo.

python bootstrap.py
bin\buidout.exe

import shlex
import subprocess
import os
import logging
from shutil import copyfile

logger = logging.getLogger(__name__)

subgrid_root = "C:\\3di\\subgrid"
subgrid_exe = os.path.join(subgrid_root, "subgridf90.exe")
copy_to_work_dir = [
	'subgrid.ini',
	'unstruc.hlp',
	'isocolour.hls',
	'land.rgb',
	'water.rgb',
	'interception.rgb',
	'land.zrgb',
	'interact.ini',
	'UNSA_SIM.inp',
	'ROOT_SIM.INP',
	'CROP_OW.PRN',
	'CROPFACT',
	'EVAPOR.GEM',
	]

	
def setup_and_run_3di(mdu_full_path):
	full_path = os.path.dirname(mdu_full_path)
	logger.info('Setting up working directory in %s...' % full_path)

	# Go to working dir
	os.chdir(full_path)	

	# Copy default files
	for filename in copy_to_work_dir:
		dst_filename = os.path.join(full_path, filename)
		if not os.path.exists(dst_filename):
			src_filename = os.path.join(subgrid_root, filename)
			logger.info('Copying %s from defaults...' % filename)
			copyfile(src_filename, dst_filename)
		else:
			logger.info('%s exists, ok.' % filename)
	# TODO: Extra checks, update files, etc.
	
	# subgrid.ini
	
	# Run 
	os.system('%s %s' % (subgrid_exe, mdu_full_path))
	
	# Results in full_path + subgrid_map.nc
	# *.tim is also produced.
	
	
def main():
	mdu_full_path = "Z:\\git\\sites\\flooding\\driedi\\Vecht\\vecht_autostartstop.mdu"
	setup_and_run_3di(mdu_full_path)
	
	
if __name__ == '__main__':
	main()

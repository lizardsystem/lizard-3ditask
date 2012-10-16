# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import (
  print_function,
#  unicode_literals,
  absolute_import,
  division,
)

from django.core.management.base import BaseCommand
from lizard_3ditask.task_pp import post_process_detailed_3di


class Command(BaseCommand):
    args = 'Command args'
    help = 'Command help'

    def handle(self, *args, **options):
        print("Starting 3Di post processing detailed...")

	full_path = "/home/jack/git/sites/flooding/driedi/Vecht/subgrid_map.nc"
        post_process_detailed_3di(full_path)

        print("Finished.")

# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import (
  print_function,
#  unicode_literals,
  absolute_import,
  division,
)

from django.core.management.base import BaseCommand
from lizard_3ditask.task_exe import setup_and_run_3di


class Command(BaseCommand):
    args = 'Command args'
    help = 'Command help'

    def handle(self, *args, **options):
        print("Starting 3Di task...")

	mdu_full_path = "Z:\\git\\sites\\flooding\\driedi\\Vecht\\vecht_autostartstop.mdu"
        setup_and_run_3di(mdu_full_path)

        print("Finished.")

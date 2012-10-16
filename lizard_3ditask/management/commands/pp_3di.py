# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import (
  print_function,
#  unicode_literals,
  absolute_import,
  division,
)

from django.core.management.base import BaseCommand
from lizard_3ditask.task_pp import post_process_3di


class Command(BaseCommand):
    args = 'Command args'
    help = 'Command help'

    def handle(self, *args, **options):
        print("Starting 3Di post processing...")

	full_path = "~/git/sites/flooding/driedi/Vecht/vecht_autostartstop.mdu"
        post_process_3di(full_path)

        print("Finished.")

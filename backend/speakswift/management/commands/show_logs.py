from django.core.management.base import BaseCommand
from config.settings import BASE_DIR
from pathlib import Path

import os

class Command(BaseCommand):
    help = 'Shows last N lines of the log file'

    def add_arguments(self, parser):
        parser.add_argument('lines', type=int, nargs='?', default=50)

    def handle(self, *args, **options):
        log_file = BASE_DIR.joinpath(Path('logs')).joinpath(Path('debug.log'))
        lines = options['lines']

        if not os.path.exists(log_file):
            self.stdout.write(self.style.ERROR('Log file not found'))
            return

        with open(log_file, 'r') as f:
            content = f.readlines()
            last_lines = content[-lines:]
            for line in last_lines:
                self.stdout.write(line.strip()) 
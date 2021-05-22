from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    """Check if db is up before starting the django server"""

    help = "Check if db is up before starting the django server"
    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))

    

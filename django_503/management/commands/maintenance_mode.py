"""Management utility to enable/disable maintenance mode"""

import sys
from django.core.management.base import BaseCommand, CommandError
from django_503.maintenance import enable, disable, is_enabled


class Command(BaseCommand):

    """
    Used to disable/enable maintenance mode

    Possible commands:

    enable -- enable maintenance mode
    disable -- disable maintenance mode
    status -- return maintenance mode status
    help -- print this help message
    """

    help = __doc__
    args = "[command]"

    def get_command(self, commands):
        if len(commands) > 1:
            raise CommandError('Enter a single command')
        return commands[0] if commands else 'status'

    def handle(self, *commands, **options):
        command = self.get_command(commands)
        if command == 'enable':
            self.enable()
        elif command == 'disable':
            self.disable()
        elif command == 'status':
            self.print_status()
        elif command == 'help':
            self.print_usage()
        else:
            self.stderr.write("Command not understood: %s\n" % command)
            sys.exit(1)

    def enable(self):
        enable()
        self.print_status("enabled")

    def disable(self):
        disable()
        self.print_status("disabled")

    def print_status(self, status=None):
        if status is None:
            status = "enabled" if is_enabled() else "disabled"
        self.stdout.write("Maintenance mode: %s\n" % status)

    def print_usage(self):
        help_args = (sys.argv[0], 'maintenance_mode')
        self.print_help(*help_args)

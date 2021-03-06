#
# samba-itest - utility to diagnose domain controller problems
#
# Copyright (C) 2019-2020 BaseALT Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from .config import read_config
from .import_wrapper import try_import
from .report.report import Report

class Diag:
    def __init__(self, diag_config, report):
        self.config = read_config(diag_config)

        self.type = 'controller'
        if 'type' in self.config:
            self.type = self.config['type']

        self.report = Report(report, self.type)

    def run(self):
        self.check_packages()
        self.check_files()
        self.check_systemd()
        self.check_samba()
        self.check_ports()

        self.report.dump()

    def check_packages(self):
        mod_rpm = try_import('rpm')
        if mod_rpm:
            from diag.checker.rpm import (
                is_rpm_installed,
                rpm_files_correct
            )
            if 'packages' in self.config:
                for pkg in self.config['packages']:
                    if is_rpm_installed(pkg):
                      self.report.add('package', pkg, rpm_files_correct(pkg))

    def check_files(self):
        from diag.checker.files import file_present
        if 'files_present' in self.config:
            for fpath in self.config['files_present']:
                self.report.add('file', fpath, file_present(fpath))

    def check_systemd(self):
        mod_dbus = try_import('dbus')
        if mod_dbus:
            import diag.checker.systemd

    def check_samba(self):
        mod_samba = try_import('samba')
        if mod_samba:
            import diag.checker.samba

    def check_ports(self):
        from diag.checker.network import is_port_opened
        if 'localhost_ports_opened' in self.config:
            for port_struct in self.config['localhost_ports_opened']:
                descr = port_struct['description']
                port = port_struct['port']

                if is_port_opened(port):
                    self.report.add('port', '{} port ({}) is opened'.format(descr, port), 'true')
                    print('{} port ({}) is opened'.format(descr, port))
                else:
                    self.report.add('port', '{} port ({}) is opened'.format(descr, port), 'false')
                    print('{} port ({}) is closed'.format(descr, port))


#
# samba-itest - Samba integration testing utilit
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


import subprocess
import rpm


def is_rpm_installed(rpm_name):
    '''
    Check if the package named 'rpm_name' is installed

    :param rpm_name: - string representing RPM name

    :return: True in case the package is installed and False otherwise
    '''
    ts = rpm.TransactionSet()
    pm = ts.dbMatch('name', rpm_name)

    if pm.count() > 0:
        print('RPM is installed: {}'.format(rpm_name))
        return True

    print('RPM is not installed: {}'.format(rpm_name))
    return False

def rpm_files_correct(rpm_name):
    '''
    Check if files belonging to RPM are not broken (have correct
    checksums and no other changes)

    :param rpm_name: - string representing RPM name

    :return: True in case the package is installed and False otherwise
    '''
    result = subprocess.call(['/usr/bin/rpm', '-V', rpm_name])

    if result == 0:
        print('RPM {} files are correct'.format(rpm_name))
        return True

    print('RPM {} files have changes'.format(rpm_name))
    return False


#
# samba-itest - Samba integration testing utility
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

import importlib

def try_import(module_name):
    '''
    Try to import module

    :param module_name: Module name to import
    '''
    result = None

    try:
        result = importlib.import_module(module_name)
        print('Loaded Python 3 module {}'.format(module_name))
    except ModuleNotFoundError as exc:
        print('Unable to import module {}'.format(module_name))

    return result


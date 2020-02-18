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

from pathlib import Path

def file_present(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        print('Path {} exists'.format(file_path.resolve()), end='')
        if file_path.is_file():
            print(' and is a regular file')
            return True
        if file_path.is_symlink():
            print(' and is a symbolic link')
            return True
        print(' and is not a regular file nor symlink')
    else:
        print('Path {} does not exist'.format(file_path.resolve()))

    return False


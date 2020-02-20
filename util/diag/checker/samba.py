#
# samba-itest - Samba interation testing utility
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


import optparse
import subprocess
from samba import getopt as options

class SambaCreds:
    def __init__(self):
        self.parser = optparse.OptionParser('Samba config checker')
        self.sambaopts = options.SambaOptions(self.parser)
        self.credopts = options.CredentialsOptions(self.parser)
        self.lp = self.sambaopts.get_loadparm()
        self.creds = self.credopts.get_credentials(self.lp, fallback_machine=True)

def smb_check_config(screds):
    result = subprocess.call(['/usr/bin/testparm', '-s'])

    if result == 0:
        return True

    return False

def smb_is_dc(screds):
    servrole = str(screds.lp.server_role())

    if (servrole == 'ROLE_STANDALONE') or (servrole == 'ROLE_ACTIVE_DIRECTORY_DC'):
        return True

    return False


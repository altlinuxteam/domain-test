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
from xml.etree import ElementTree as ET
from xml.dom import minidom

class Report:
    def __init__(self, report_file, machine_type):
      self.report_file = report_file
      self.type = machine_type
      self.report = ET.Element('report')

      mtype = ET.SubElement(self.report, 'type')
      mtype.text = self.type

    def add(self, test_id, description, result):
      elem = ET.SubElement(self.report, test_id)
      elem.text = '{}: {}'.format(description, str(result))

    def dump(self):
        serial = ET.tostring(self.report, 'utf-8')
        pretty = minidom.parseString(serial).toprettyxml(indent='    ')

        with open(self.report_file,'w') as f:
            f.write(pretty)

#  Copyright (C) 2019-2022 Xcalibyte (Shenzhen) Limited.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import unittest

from common.CommandLineUtility import CommandLineUtility
from common.XcalLogger import XcalLogger


class BasicCase(unittest.TestCase):
    def setUp(self):
        self.logger = XcalLogger("CommandLineUtilityTest", "BasicCase")

    def test_echo_success(self):
        rc = CommandLineUtility.bash_execute("echo ok", 1.0, self.logger, "test.log")
        self.assertEqual(0, rc)

    def test_not_found_command(self):
        rc = CommandLineUtility.bash_execute("makes ome unknown program ok", 1.0, self.logger, "test.log")
        self.assertNotEqual(0, rc)

    def test_temp_logfile(self):
        rc = CommandLineUtility.bash_execute("echo ok", 1.0, self.logger)
        self.assertEqual(0, rc)

if __name__ == '__main__':
    unittest.main()

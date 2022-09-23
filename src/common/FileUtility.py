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


import os

from common.CommonGlobals import TaskErrorNo
from common.XcalException import XcalException
from common.XcalLogger import XcalLogger


class FileUtility(object):
    def __init__(self, logger: XcalLogger):
        self.logger = logger
        self.dir_stack = []

    def goback_dir(self):
        """
        Go back one level dir in stack, OS-Independent
        :return: None
        """
        # Reading data back
        if len(self.dir_stack) >= 1:
            last_dir = self.dir_stack.pop()
            self.logger.info("Going back dir_stack", last_dir)
            self.dir_stack.append(os.curdir)
            os.chdir(last_dir)
        else:
            raise XcalException("FileUtility", "goback_dir", "Cannot pop the directory stack",
                                TaskErrorNo.E_FILEUTIL_DIRSTACK)

    def goto_dir(self, new_workdir: str):
        """
        Goto Another dir, while pushing the current dir to stack OS-Independent
        :param new_workdir: str
        :return:  None
        """
        # Reading data back
        self.logger.info("Change working directory", new_workdir)
        self.dir_stack.append(os.path.abspath(os.curdir))
        os.chdir(new_workdir)

    @staticmethod
    def check_dir_exist_readable(dirname):
        if (not os.path.exists(dirname)) or (not os.path.isdir(dirname)):
            raise XcalException("FileUtility", "check_dir_exist_readable",
                                "Dir %s does not exist or is not a valid directory" % dirname,
                                TaskErrorNo.E_COMMON_FOLDER_NONEXIST)

        if not os.access(dirname, os.W_OK | os.R_OK):
            raise XcalException("FileUtility", "check_dir_exist_readable", "Directory %s is not readable/writable" % dirname,
                                TaskErrorNo.E_COMMON_FOLDER_PERMISSION)
        pass
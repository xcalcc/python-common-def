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

from common.XcalLogger import XcalLogger


class XcalException(Exception):
    def __init__(self, service_name: str, operation_name: str, message: any, err_code, hint: str = None, info:dict = None):
        self.service = service_name
        self.operation = operation_name
        self.message = message
        self.err_code = err_code
        self.info = info
        self.logger = XcalLogger
        if hint is not None:
            self.hint = hint
        else:
            self.hint = ""
        super(XcalException).__init__()

    def __str__(self):
        return "service_name: %s, operation_name: %s, message: %s, error_code: %s" % (self.service, self.operation, self.message, self.err_code)


class XcalExceptionPrinter(object):
    def __init__(self, exception):
        if exception is None or type(exception) is not XcalException:
            self.exception = None
            return
        else:
            self.exception = exception

    def print_error(self):
        print(
            "[ErrNo]:" + self.exception.err_code.__str__() + ", " + "[ErrMsg]:" + self.exception.message + ", " + "[Hint]:" + self.exception.hint)

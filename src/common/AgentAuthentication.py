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


import re

from scanTaskService.Config import NAME_LEN_MAX


class AgentValueVerifier(object):
    @staticmethod
    def is_name_valid(name:str):
        if name is None or len(name) > NAME_LEN_MAX:
            return False
        return re.match("^[a-zA-Z0-9-_]+$", name) is not None
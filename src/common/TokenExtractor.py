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


TOKEN_FIELD_NAME = "token"


class TokenExtractor(object):
    def __init__(self, config):
        self.config = config
        pass

    def get_token_str(self):
        return 'Bearer %s' % self.config.get("token")

    def get_xvsa_token(self):
        return self.config.get("token")

    def get_plain_token(self):
        return self.config.get("token")

    def valid(self):
        return self.config.get("token") is not None


class TokenInjector(object):
    def __init__(self, config:dict, task_config):
        self.config = config.copy()
        self.config["token"] = TokenExtractor(task_config).get_plain_token()

    def get_injected(self):
        return self.config


class TokenObjectCreator(object):
    def __init__(self):
        pass

    def inject_object(self, config:dict, token:str):
        config["token"] = token
        return config

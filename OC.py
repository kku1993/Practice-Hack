# Copyright 2013 OpenCurriculum, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An OpenCurriculum API Python library.

Tools for interacting with the OpenCurriculum API for obtaining resources.
"""

__author__ = 'varun@theopencurriculum.org (Varun Arora)'


class Article():
    def list(self, limit=10):
        return self.get('articles/list/?limit=' + str(limit))

    def get(self, url):
        import httplib
        import json

        request = httplib.HTTPConnection('theopencurriculum.org', 80)
        request.connect()
        request.request(
            'GET', '/api/' + url)
        response = request.getresponse()
        return json.loads(response.read())


class OC():
    articles = Article()
#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import unittest
from testsearch.test_matcher import _TestSearchTest


class TestTestSorter(_TestSearchTest, unittest.TestCase):

    def test_exact_match_is_better_than_partial(self):
        match_text = 'exact'
        exact_match = self._match(match_text, name='exact')
        with_something_extra_after_match = self._match(match_text, name='exact jotain')
        with_something_extra_before_match = self._match(match_text, name='jotain exact')
        starting_with_match = self._match(match_text, name='exact_foo')
        a_and_match = self._match(match_text, name='aexact')
        z_and_match = self._match(match_text, name='zexact')
        self.assertGreater(with_something_extra_after_match, exact_match)
        self.assertGreater(with_something_extra_before_match, with_something_extra_after_match)
        self.assertGreater(starting_with_match, with_something_extra_before_match)
        self.assertGreater(a_and_match, starting_with_match)
        self.assertGreater(z_and_match, a_and_match)

    def test_name_is_better_than_doc(self):
        name_match = self._match('name', name='name')
        doc_match = self._match('doc', doc='doc')
        self.assertGreater(doc_match, name_match)

    def test_name_is_better_than_tag(self):
        name_match = self._match('name', name='name')
        tag_match = self._match('tag', tags=['tag'])
        self.assertGreater(tag_match, name_match)

    def test_tag_is_better_than_doc(self):
        tag_match = self._match('tag', tags=['tag'])
        doc_match = self._match('doc', doc='doc')
        self.assertGreater(doc_match, tag_match)

if __name__ == '__main__':
    unittest.main()
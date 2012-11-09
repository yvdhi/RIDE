import tempfile
import unittest
import os
import datafilereader
from robotide.controller.filecontrollers import TestDataDirectoryController, ExcludedDirectoryController


class TestExcludesLogic(unittest.TestCase):

    def setUp(self):
        self.chief = datafilereader.construct_chief_controller(datafilereader.SIMPLE_TEST_SUITE_PATH, tempfile.gettempdir())

    def tearDown(self):
        p = self.chief._settings.excludes._exclude_file_path
        if os.path.exists(p):
            os.remove(p)

    def _get_resource_dir(self):
        return datafilereader.get_ctrl_by_name(datafilereader.SIMPLE_TEST_SUITE_INNER_RESOURCE_DIR, self.chief.datafiles)

    def test_excluding_and_including(self):
        resource_dir = self._get_resource_dir()
        self.assertEqual(resource_dir.__class__, TestDataDirectoryController)
        resource_dir.exclude()
        resource_dir = self._get_resource_dir()
        self.assertEqual(resource_dir.__class__, ExcludedDirectoryController)
        resource_dir.remove_from_excludes()
        resource_dir = self._get_resource_dir()
        self.assertEqual(resource_dir.__class__, TestDataDirectoryController)


if __name__ == '__main__':
    unittest.main()
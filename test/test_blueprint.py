#!/usr/bin/env python

import os
import sys
import unittest
import pdb

from context import blueprint

class TestSuite(unittest.TestCase):
    def test_basicFolder(self):
        result = ["normalFolder1", "normalFolder2"]
        self.assertListEqual(
            blueprint.getPathsToCreate("blueprint1", "", []), result
        )

    def test_invalidEnv(self):
        os.environ["MYTYPE"] = ""
        result = []
        self.assertListEqual(
            blueprint.getPathsToCreate("blueprint2", "", []), result
        )

    def test_basicTypeFolder(self):
        os.environ["MYTYPE"] = "myFolder"
        result = ["myFolder"]
        self.assertListEqual(
            blueprint.getPathsToCreate("blueprint2", "", []), result
        )

    def test_specificTypeFolder(self):
        os.environ["TYPEFOLDER"] = "another"
        result = ["another", "another/newFolder"]
        self.assertListEqual(
            blueprint.getPathsToCreate("blueprint3", "", []), result
        )

    def test_deepFolder(self):
        os.environ["TYPEFOLDER"] = "other"
        os.environ["OTHERTYPEFOLDER"] = "blah"
        result = ["normalFolder", 
            "normalFolder2",
            "normalFolder/other",
            "normalFolder/other/blah"
        ]
        self.assertListEqual(
            blueprint.getPathsToCreate("blueprint4", "", []), sorted(result)
        )

 
if __name__ == "__main__":
    unittest.main()

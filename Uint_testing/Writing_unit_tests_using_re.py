#!/usr/bin/env python3

# importing rearrange_name

from rearrang_name import rearrange_name

import unittest

class TestRearrange(unittest.TestCase): # inherating from unittest.TestCase 
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    # Adding another test case to check if the string is empty
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()
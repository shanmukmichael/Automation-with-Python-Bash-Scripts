#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    """Testing...."""
def test_basic(self):
    testcase = "michael ,shanmuk"
    expected = "Shanmuk Michael"
    self.assertEqual(rearrange_name(testcase), expected)

def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

def test_double_name(self):
    testcase = "is Good, P.Shanmuk"
    expected = "P.Shanmuk is Good"
    self.assertEqual(rearrange_name(testcase), expected)

def test_double_name(self):
    testcase = "Shanmuk"
    expected = "Shanmuk"
    self.assertEqual(rearrange_name(testcase), expected)
unittest.main()

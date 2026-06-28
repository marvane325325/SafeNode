# test_safenode.py
"""
Tests for SafeNode module.
"""

import unittest
from safenode import SafeNode

class TestSafeNode(unittest.TestCase):
    """Test cases for SafeNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SafeNode()
        self.assertIsInstance(instance, SafeNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SafeNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

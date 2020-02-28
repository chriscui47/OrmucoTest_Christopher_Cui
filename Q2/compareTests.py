import unittest
from compare import compare

class TestCompare(unittest.TestCase):
    def test_numbers(self):
        # GREATER

        version1 = "1.1.3"
        version2 = "1.1.2"
        self.assertEqual(compare(version1, version2), version1 + " is GREATER than " + version2)

        version1 = "2.113.3"
        version2 = "2.113.2"
        self.assertEqual(compare(version1, version2), version1 + " is GREATER than " + version2)

        version1 = "2.5.1"
        version2 = "2.4.0"
        self.assertEqual(compare(version1, version2), version1 + " is GREATER than " + version2)

        # ------- LESSER --------
        version1 = "2.1.1"
        version2 = "2.1.2"
        self.assertEqual(compare(version1, version2), version1 + " is SMALLER than " + version2)

        version1 = "2.1.1"
        version2 = "2.10.1"
        self.assertEqual(compare(version1, version2), version1 + " is SMALLER than " + version2)

        version1 = "3.0.1"
        version2 = "3.0.2"
        self.assertEqual(compare(version1, version2), version1 + " is SMALLER than " + version2)
        # EQUAL
        version1 = "3.3.3"
        version2 = "3.3.3"
        self.assertEqual(compare(version1, version2), version1 + " is EQUAL to " + version2)

        version1 = "200.144"
        version2 = "200.144"
        self.assertEqual(compare(version1, version2), version1 + " is EQUAL to " + version2)

    def test_invalid_input(self):
        # ------- INVALID VERSION 1 --------

        # Cannot have . with no subsequent number
        version1 = "3.3.3"
        version2 = "2."
        self.assertEqual(compare(version1, version2), "Wrong format")

        # Cannot have . before a number
        version1 = "2.2.2"
        version2 = ".2"
        self.assertEqual(compare(version1, version2), "Wrong format")

        # Cannot have letters
        version1 = "2.2"
        version2 = "sfasfdpk.asdfsa"
        self.assertEqual(compare(version1, version2), "Wrong format")

        # Cannot have negative
        version1 = "2.2"
        version2 = "-1321.1"
        self.assertEqual(compare(version1, version2), "Negative value versions not accepted")


        # ------- INVALID BOTH VERSIONS --------
        
        #Cannot have none
        #cannot be empty
        version1 = None
        version2 = ""
        self.assertEqual(compare(version1, version2), "Invalid empty input")

    

if __name__ == '__main__':
    unittest.main()
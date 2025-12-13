"""Unit tests for the sensitive data checker script."""

# pylint: disable=missing-function-docstring,invalid-name
import os
import unittest
from pathlib import Path
from unittest.mock import patch

import tempfile

from coding_standards.pre_commit.sensitive_data_check import check_file, main


class TestSensitiveDataCheck(unittest.TestCase):
    """Test suite for sensitive data checker."""

    def setUp(self):
        """Set up temporary directory."""
        # Create a temporary directory
        # pylint: disable=consider-using-with
        self.test_dir = tempfile.TemporaryDirectory()
        self.root_path = Path(self.test_dir.name)

    def tearDown(self):
        """Clean up temporary directory."""
        # Cleanup
        self.test_dir.cleanup()

    def create_file(self, content):
        """Helper to create a file with given content."""
        file_descriptor, path = tempfile.mkstemp(dir=self.root_path, text=True)
        with os.fdopen(file_descriptor, "w", encoding="utf-8") as file_handle:
            file_handle.write(content)
        return path

    def test_clean_file(self):
        """Test a clean file works."""
        content = """
        def hello():
            print("Hello world")
        """
        path = self.create_file(content)
        self.assertFalse(check_file(path), "Clean file should not trigger detection")

    def test_hl7_detection(self):
        """Test HL7 MSH segment detection."""
        # pylint: disable=line-too-long
        content = "MSH|^~\\&|EPIC|EPICADT|SMS|SMSADT|199912271408|CHARRIS|ADT^A04|1817457|D|2.5|\nPID||0493575^^^2^ID 1|454721||DOE^JOHN^^^^|DOE^JOHN^^^^|19480203|M||B|254 MYSTREET AVE^^MYTOWN^OH^44123^USA||(216)123-4567|||M|NON|400003403~1129086|"
        path = self.create_file(content)
        self.assertTrue(check_file(path), "HL7 MSH segment should be detected")

    def test_mds_detection(self):
        """Test MDS assessment detection."""
        # pylint: disable=line-too-long
        content = "Resident Identiier Date\n999999\nLASTNAME, FIRSTNAME\n11/30/2025\nSection A - Identification Information\nA0050. Type of Record"
        path = self.create_file(content)
        self.assertTrue(
            check_file(path), "MDS 'Section A - Identification Information' should be detected"
        )

    def test_phi_keywords(self):
        """Test PHI keyword detection."""
        content = "My Social Security Number is 123-456-7890"
        path = self.create_file(content)
        self.assertTrue(check_file(path), "Social Security Number keyword should be detected")

    def test_mds_code_pattern(self):
        """Test MDS code pattern detection."""
        content = "A0100. Facility Provider Numbers"
        path = self.create_file(content)
        self.assertTrue(check_file(path), "MDS code pattern A0100. should be detected")

    def test_missing_file(self):
        """Test handling of non-existent files."""
        self.assertFalse(check_file("non_existent_file.txt"), "Missing file should return False")

    def test_binary_file(self):
        """Test handling of binary files."""
        # Create a binary file
        file_descriptor, path = tempfile.mkstemp(dir=self.root_path)
        with os.fdopen(file_descriptor, "wb") as file_handle:
            file_handle.write(b"\x80\x81\x82")  # Invalid UTF-8
        self.assertFalse(check_file(path), "Binary file should return False")

    def test_main_success(self):
        """Test main function with clean file."""
        # Create a clean file
        path = self.create_file("clean content")

        with patch("sys.argv", ["prog", path]):
            with self.assertRaises(SystemExit) as context:
                main()
            self.assertEqual(context.exception.code, 0)

    def test_main_failure(self):
        """Test main function with sensitive file."""
        # Create a sensitive file
        path = self.create_file("Social Security Number")

        with patch("sys.argv", ["prog", path]):
            with self.assertRaises(SystemExit) as context:
                main()
            self.assertEqual(context.exception.code, 1)

    def test_skip_non_sensitive_extension(self):
        self.assertFalse(
            check_file(self.create_file("just text")), "Non-sensitive file should not be skipped"
        )


if __name__ == "__main__":
    unittest.main()

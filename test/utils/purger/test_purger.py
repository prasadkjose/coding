"""Test module for purger.py using pytest"""

import logging

# Import the purger module directly
import sys
from unittest.mock import patch

import pytest

from utils.purger import purge_directories

sys.path.insert(0, "/home/prasad/projects/practice")


class TestPurger:
    """Test class for purger module"""

    def test_purge_directories_basic_functionality(self, tmp_path):
        """Test basic directory purging functionality"""
        # Create test directories
        test_dirs = ["test_dir1", "test_dir2", "test_dir3"]
        for dir_name in test_dirs:
            (tmp_path / dir_name).mkdir()
            # Add some files to make sure directories are not empty
            (tmp_path / dir_name / "file.txt").write_text("test content")

        # Create system directories that should be preserved
        system_dirs = ["utils", ".git", "node_modules"]
        for dir_name in system_dirs:
            (tmp_path / dir_name).mkdir()
            (tmp_path / dir_name / "file.txt").write_text("system content")

        # Run purge
        purge_directories(str(tmp_path))

        # Check that test directories were deleted
        for dir_name in test_dirs:
            assert not (
                tmp_path / dir_name
            ).exists(), f"Directory {dir_name} should have been deleted"

        # Check that system directories were preserved
        for dir_name in system_dirs:
            assert (
                tmp_path / dir_name
            ).exists(), f"System directory {dir_name} should have been preserved"
            assert (
                tmp_path / dir_name / "file.txt"
            ).exists(), f"Content in {dir_name} should have been preserved"

    def test_purge_directories_with_files(self, tmp_path):
        """Test purging directories that contain files and subdirectories"""
        # Create a directory with nested structure
        nested_dir = tmp_path / "nested_test"
        nested_dir.mkdir()
        (nested_dir / "file1.txt").write_text("content1")
        (nested_dir / "subdir").mkdir()
        (nested_dir / "subdir" / "file2.txt").write_text("content2")

        # Create another test directory
        simple_dir = tmp_path / "simple_test"
        simple_dir.mkdir()
        (simple_dir / "simple_file.txt").write_text("simple content")

        # Run purge
        purge_directories(str(tmp_path))

        # Both directories should be deleted with all contents
        assert not nested_dir.exists(), "Nested directory should have been deleted"
        assert not simple_dir.exists(), "Simple directory should have been deleted"

    def test_purge_directories_empty_directory(self, tmp_path):
        """Test purging an empty directory"""
        # No directories to delete, should not raise any errors
        purge_directories(str(tmp_path))

        # Directory should still exist and be empty
        assert tmp_path.exists()
        assert len(list(tmp_path.iterdir())) == 0

    def test_purge_directories_preserves_system_dirs(self, tmp_path):
        """Test that system directories are properly preserved"""
        # Create all system directories that should be preserved
        system_dirs = ["utils", "venv", ".git", ".vscode", "node_modules"]
        for dir_name in system_dirs:
            (tmp_path / dir_name).mkdir()
            (tmp_path / dir_name / "important_file.txt").write_text(
                f"Important content for {dir_name}"
            )

        # Create some regular directories to be deleted
        regular_dirs = ["temp", "cache", "logs"]
        for dir_name in regular_dirs:
            (tmp_path / dir_name).mkdir()
            (tmp_path / dir_name / "temp_file.txt").write_text(
                f"Temporary content for {dir_name}"
            )

        # Run purge
        purge_directories(str(tmp_path))

        # System directories should be preserved
        for dir_name in system_dirs:
            assert (
                tmp_path / dir_name
            ).exists(), f"System directory {dir_name} should be preserved"
            assert (
                tmp_path / dir_name / "important_file.txt"
            ).exists(), f"Content in {dir_name} should be preserved"

        # Regular directories should be deleted
        for dir_name in regular_dirs:
            assert not (
                tmp_path / dir_name
            ).exists(), f"Regular directory {dir_name} should be deleted"

    def test_purge_directories_logging(self, tmp_path, caplog):
        """Test that logging works correctly"""
        # Create test directories
        (tmp_path / "test_dir1").mkdir()
        (tmp_path / "test_dir2").mkdir()
        (tmp_path / "utils").mkdir()  # Should be preserved

        with caplog.at_level(logging.INFO):
            purge_directories(str(tmp_path))

        # Check that appropriate log messages were generated
        log_messages = caplog.text

        # Should log starting operation
        assert "Starting purge operation" in log_messages
        assert "Found" in log_messages
        assert "Purge operation completed" in log_messages

        # Should log deletion of test directories
        assert "Deleting directory: test_dir1" in log_messages
        assert "Deleting directory: test_dir2" in log_messages

        # Should log skipping of system directories
        assert "Skipping directory: utils" in log_messages

    @patch("shutil.rmtree")
    def test_purge_directories_permission_error(self, mock_rmtree, tmp_path, caplog):
        """Test handling of permission errors"""
        # Mock shutil.rmtree to raise PermissionError
        mock_rmtree.side_effect = PermissionError("Permission denied")

        # Create test directory
        (tmp_path / "test_dir").mkdir()

        with caplog.at_level(logging.ERROR):
            purge_directories(str(tmp_path))

        # Should log the error
        assert "Permission denied deleting test_dir" in caplog.text

    @patch("shutil.rmtree")
    def test_purge_directories_os_error(self, mock_rmtree, tmp_path, caplog):
        """Test handling of OSError"""
        # Mock shutil.rmtree to raise OSError
        mock_rmtree.side_effect = OSError("Disk full")

        # Create test directory
        (tmp_path / "test_dir").mkdir()

        with caplog.at_level(logging.ERROR):
            purge_directories(str(tmp_path))

        # Should log the error
        assert "Error deleting test_dir: Disk full" in caplog.text

    def test_purge_directories_mixed_content(self, tmp_path):
        """Test purging with a mix of files and directories"""
        # Create directories
        (tmp_path / "dir1").mkdir()
        (tmp_path / "dir2").mkdir()

        # Create files (should not be affected)
        (tmp_path / "file1.txt").write_text("file content")
        (tmp_path / "file2.py").write_text("print('hello')")

        # Create system directory
        (tmp_path / "utils").mkdir()

        # Run purge
        purge_directories(str(tmp_path))

        # Directories should be deleted
        assert not (tmp_path / "dir1").exists()
        assert not (tmp_path / "dir2").exists()

        # Files should remain
        assert (tmp_path / "file1.txt").exists()
        assert (tmp_path / "file2.py").exists()

        # System directory should be preserved
        assert (tmp_path / "utils").exists()

    def test_purge_directories_regex_patterns(self, tmp_path):
        """Test that regex patterns for system directories work correctly"""
        # Create directories that should match system patterns
        dirs_to_preserve = ["utils", "venv", ".hidden", ".config", "node_modules"]
        for dir_name in dirs_to_preserve:
            (tmp_path / dir_name).mkdir()

        # Create directories that should be deleted
        dirs_to_delete = ["temp", "cache", "build", "dist", "logs"]
        for dir_name in dirs_to_delete:
            (tmp_path / dir_name).mkdir()

        # Run purge
        purge_directories(str(tmp_path))

        # Check preservation
        for dir_name in dirs_to_preserve:
            assert (
                tmp_path / dir_name
            ).exists(), f"Directory {dir_name} should be preserved"

        # Check deletion
        for dir_name in dirs_to_delete:
            assert not (
                tmp_path / dir_name
            ).exists(), f"Directory {dir_name} should be deleted"


if __name__ == "__main__":
    # Allow running this test file directly
    pytest.main([__file__, "-v"])

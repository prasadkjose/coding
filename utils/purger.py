"""Purger module"""

import os
import shutil
import re
import logging

logger = logging.getLogger(__name__)


def purge_directories(path):
    """
    Delete all directories in the current path except those matching patterns in system_dirs.
    Recursively deletes all contents of excluded directories.
    """
    # Dirs needed for the project
    system_dirs = ["utils", "venv", r"^\.", "node_modules"]

    logger.info("Starting purge operation in: %s", path)

    # Get all items in current directory
    items = os.listdir(path)
    print(items)

    # Filter to get only directories
    directories = [item for item in items if os.path.isdir(os.path.join(path, item))]

    logger.info("Found %d directories to process", len(directories))

    deleted_count = 0
    skipped_count = 0

    for directory in directories:
        dir_path = os.path.join(path, directory)

        # Check if directory should be excluded
        should_skip = False
        for pattern in system_dirs:
            if re.match(pattern, directory):
                logger.info(
                    "Skipping directory: %s (matches pattern: %s)", directory, pattern
                )
                should_skip = True
                skipped_count += 1
                break

        if should_skip:
            continue

        # Delete the directory and all its contents
        try:
            logger.info("Deleting directory: %s", directory)
            shutil.rmtree(dir_path)
            deleted_count += 1
            logger.info("Successfully deleted: %s", directory)
        except PermissionError as e:
            logger.error("Permission denied deleting %s: %s", directory, e)
        except OSError as e:
            logger.error("Error deleting %s: %s", directory, e)
    logger.info(
        "Purge operation completed. Deleted: %d, Skipped: %d",
        deleted_count,
        skipped_count,
    )

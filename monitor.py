"""
File Watcher and Backup Script

This script monitors a specified folder (`watched_folder`) for any file system events
(such as file creation, modification, deletion, or movement) using the `watchdog` library.

When a new file is created in the watched folder:
    - It is automatically copied to a backup folder (`../backup`).
    - The event is logged in a `Log.txt` file located one directory above the watched folder.

Features:
    - Real-time monitoring of file system changes.
    - Automatic backup of newly created files.
    - Logging of all detected events with timestamps.

Requirements:
    - watchdog (install via `pip install watchdog`)

Author: SirLuciferZ
Date: 2025/09/02
"""

import shutil
import time
from datetime import datetime
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set working directory to the script's location
BASE_DIR = Path(__file__).resolve().parent
WATCHED_FOLDER = BASE_DIR / "watched_folder"
BACKUP_FOLDER = BASE_DIR / "backup"
LOG_FILE = BASE_DIR / "Log.txt"


BACKUP_FOLDER.mkdir(exist_ok=True)


class MyEventHandler(FileSystemEventHandler):  # pylint: disable=too-few-public-methods
    """
    Custom event handler for monitoring file system changes.

    This class extends `FileSystemEventHandler` from the watchdog library
    and overrides the `on_any_event` method to handle all file system events.

    Behavior:
        - Prints event details to the console.
        - If a file is created, it is copied to the backup folder.
        - Logs all events to `Log.txt`.

    Methods:
        on_any_event(event: FileSystemEvent):
            Handles any file system event (create, modify, delete, move).
    """

    def on_any_event(self, event):
        """
        Handle any file system event.

        Args:
            event (FileSystemEvent): The event object containing details
                                     about the file system change.

        Actions:
            - Extracts the file path from the event.
            - Prints event details to the console.
            - If the event is a file creation, copies the file to the backup folder.
            - Appends event details to `Log.txt`.

        Notes:
            - The backup folder is located one directory above the watched folder.
            - The log file is also stored one directory above the watched folder.
        """

        if event.is_directory:
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src_path = Path(event.src_path)
        rel_path = src_path.relative_to(WATCHED_FOLDER)

        print(f"\n{rel_path} {event.event_type} from {src_path}\n")

        if event.event_type == "created":
            try:
                shutil.copy(src_path, BACKUP_FOLDER)
                print(f"{rel_path} copied to Backup folder at [{now}]")
            except Exception as e:
                print(f"Failed to copy {rel_path}: {e}")

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n\n\n[{now}] {rel_path} {event.event_type} from {src_path}")


# Create event handler instance
if __name__ == "__main__":
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCHED_FOLDER), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer stopped")
    observer.join()

import os
import threading
import time
from dotenv import load_dotenv


class DownloadManager:
    """Manages multi-threaded file downloads."""

    def __init__(self, num_files, num_threads):
        self.num_files = num_files
        self.num_threads = num_threads
        self.file_groups = self._split_files()

    def _split_files(self):
        """Split files into groups using round-robin distribution."""
        groups = [[] for _ in range(self.num_threads)]

        for file_id in range(1, self.num_files + 1):
            thread_id = (file_id - 1) % self.num_threads
            groups[thread_id].append(file_id)

        return groups

    def _create_threads(self):
        """Create a thread for each file group."""
        threads = []

        for group_id, group in enumerate(self.file_groups):
            thread = threading.Thread(
                target=self._download, args=(group,), name=f"Thread-{group_id + 1}"
            )
            threads.append(thread)

        return threads

    def start_download(self):
        """Create and start all download threads."""
        threads = self._create_threads()

        print(f"\n{'='*60}")
        print(f"Starting download with {self.num_threads} threads...")
        print(f"{'='*60}\n")

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print(f"\n{'='*60}")
        print("All downloads completed!")
        print(f"{'='*60}\n")

    def _download(self, files):
        """Download files assigned to this thread."""
        thread_name = threading.current_thread().name

        for file_id in files:
            print(f"[{thread_name}] Downloading file #{file_id}...")
            time.sleep(1)
            print(f"[{thread_name}] ✓ File #{file_id} completed")


def main():

    load_dotenv()

    num_files = int(os.getenv("NUMBER_OF_FILES", 100))
    num_threads = int(input("Enter number of threads: "))

    manager = DownloadManager(num_files, num_threads)
    manager.start_download()


if __name__ == "__main__":
    main()

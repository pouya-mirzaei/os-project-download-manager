from dotenv import load_dotenv
import os

import threading
import time

load_dotenv()

num_files = int(os.getenv("NUMBER_OF_FILES", 100))


class DownloadManager:
    def __init__(self, num_files, num_threads):
        self.num_files = num_files
        self.num_threads = num_threads
        self.file_groups = self._split_files()

    def _split_files(self):

        groups = [[] for _ in range(self.num_threads)]

        for file_id in range(1, self.num_files + 1):
            thread_id = (file_id - 1) % self.num_threads
            groups[thread_id].append(file_id)

        return groups

    def _create_threads(self):
        # For each group we will create a thread

        threads = []

        for group_id in range(self.num_threads):
            group = self.file_groups[group_id]
            thread = threading.Thread(
                target=self.download, args=[group], name=f"{group_id + 1}"
            )
            threads.append(thread)

        return threads

    def start_download(self):
        # Create the threads
        threads = self._create_threads()

        for thread in threads:
            thread.start()

    def download(self, files):
        current_thread = threading.current_thread()

        for f in files:
            # Simulating the download process with time.sleep()
            print(f"Thread #{current_thread.name}: Start download of file #{f}")
            time.sleep(3)

            print(f"Thread #{current_thread.name}: Finish download of file #{f}")


# Get input
num_threads = int(input("Enter number of threads : "))

# Create download manager and split files
manager = DownloadManager(num_files, num_threads)


# start downloading the files
manager.start_download()

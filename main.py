from dotenv import load_dotenv
import os


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


# Get input
num_threads = int(input("Enter number of threads : "))

# Create download manager and split files
manager = DownloadManager(num_files, num_threads)


# print(manager.file_groups)
# for group in manager.file_groups:
#     print(len(group))

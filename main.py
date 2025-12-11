import os
import threading
import time
from datetime import datetime
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Color palette for threads
COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX,
]


class DownloadManager:
    """Manages multi-threaded file downloads."""

    def __init__(self, num_files, num_threads):
        self.num_files = num_files
        self.num_threads = num_threads
        self.file_groups = self._split_files()
        self.thread_colors = {}
        self.start_time = None
        self.end_time = None

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
            # Assign a color to each thread
            self.thread_colors[group_id] = COLORS[(group_id) % len(COLORS)]

            thread = threading.Thread(
                target=self._download,
                args=(group, group_id),
                name=f"Thread-{group_id + 1}",
            )
            threads.append(thread)

        return threads

    def start_download(self):
        """Create and start all download threads."""
        threads = self._create_threads()

        print(f"\n{Style.BRIGHT}{'='*60}")
        print(f"Starting download with {self.num_threads} threads...")
        print(f"{'='*60}{Style.RESET_ALL}\n")

        self.start_time = time.time()

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.end_time = time.time()

        self._print_report()

    def _download(self, files, thread_id):
        """Download files assigned to this thread."""
        thread_name = threading.current_thread().name
        color = self.thread_colors[thread_id]

        for file_id in files:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(
                f"{color}[{current_time}] [{thread_name}] Downloading file #{file_id}...\n"
            )
            time.sleep(1)
            current_time = datetime.now().strftime("%H:%M:%S")
            print(
                f"{color}[{current_time}] [{thread_name}] ✓ File #{file_id} completed\n"
            )

    def _print_report(self):
        """Print a detailed report of the download process."""
        total_time = self.end_time - self.start_time

        print(f"\n{Style.BRIGHT}{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}DOWNLOAD REPORT")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Total Files: {Fore.WHITE}{self.num_files}")
        print(f"{Fore.YELLOW}Number of Threads: {Fore.WHITE}{self.num_threads}")
        print(f"{Fore.YELLOW}Total Time: {Fore.WHITE}{total_time:.2f} seconds")
        print(f"{Fore.CYAN}{'-'*60}")

        print(f"{Style.BRIGHT}{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")


load_dotenv()

num_files = int(os.getenv("NUMBER_OF_FILES", 100))
num_threads = int(input("Enter number of threads: "))

manager = DownloadManager(num_files, num_threads)
manager.start_download()

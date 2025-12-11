# 📥 Multi-threaded Download Manager

An Operating Systems course project that simulates multi-threaded file downloading using Python's `threading` module.

## 📋 Project Overview

This project demonstrates concurrent programming concepts by simulating the download of 100 files across multiple threads. Each download is simulated using a 1-second delay (`time.sleep(1)`), and the program distributes files evenly across threads using a round-robin scheduling algorithm.

## ✨ Features

- **Multi-threaded Downloads**: Distribute files across `k` threads for parallel processing
- **Round-robin Distribution**: Balanced file allocation across all threads
- **Colorful Output**: Each thread has a unique color for easy visual tracking
- **Real-time Timestamps**: Every log shows the exact time in `HH:MM:SS` format
- **Detailed Report**: Summary statistics showing performance metrics per thread
- **Environment Configuration**: Uses `.env` file for configurable parameters

## 🛠️ Technologies Used

- **Python 3.x**
- **threading**: Built-in module for concurrent execution
- **colorama**: Cross-platform colored terminal output
- **python-dotenv**: Environment variable management

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pouya-mirzaei/os-project-download-manager.git
   cd os-project-download-manager
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   NUMBER_OF_FILES=100
   ```

## 🚀 Usage

Run the program:

```bash
python main.py
```

When prompted, enter the number of threads:

```
Enter number of threads: 4
```

## 📊 Output Example

```
============================================================
Starting download with 4 threads...
============================================================

[14:30:45] [Thread-1] Downloading file #1...
[14:30:45] [Thread-2] Downloading file #2...
[14:30:45] [Thread-3] Downloading file #3...
[14:30:45] [Thread-4] Downloading file #4...
[14:30:46] [Thread-1] ✓ File #1 completed
[14:30:46] [Thread-1] Downloading file #5...
...

============================================================
DOWNLOAD REPORT
============================================================
Total Files: 100
Number of Threads: 4
Total Time: 25.03 seconds
------------------------------------------------------------

```

## 🏗️ Project Structure

```
OS-download-manager/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment configuration
├── .venv/              # Virtual environment (not tracked)
├── README.md           # Project documentation
```

## 🔧 How It Works

1. **Initialization**: The `DownloadManager` class is initialized with the total number of files and threads
2. **File Distribution**: Files are split into groups using round-robin algorithm (File 1→Thread 1, File 2→Thread 2, etc.)
3. **Thread Creation**: A separate thread is created for each group
4. **Parallel Execution**: All threads start simultaneously and download their assigned files
5. **Synchronization**: Main thread waits for all threads to complete using `join()`
6. **Report Generation**: Statistics are collected and displayed after completion

## 📈 Key Concepts Demonstrated

- **Concurrency**: Multiple threads executing simultaneously
- **Thread Synchronization**: Using `join()` to wait for thread completion
- **Load Balancing**: Round-robin distribution ensures equal workload
- **Resource Management**: Tracking thread statistics and timing
- **Process Simulation**: Using delays to simulate real-world operations

## 🎓 Learning Outcomes

This project helps understand:

- Creating and managing threads in Python
- Thread lifecycle and synchronization
- Parallel processing and performance benefits
- Race condition prevention (thread-safe operations)
- Real-world OS concepts applied in code

## 📝 Configuration

The `.env` file supports the following variables:

| Variable          | Default | Description                       |
| ----------------- | ------- | --------------------------------- |
| `NUMBER_OF_FILES` | `100`   | Total number of files to download |

## 🤝 Contributing

This is an educational project. Feel free to fork and experiment!

## 📄 License

This project is created for educational purposes as part of an Operating Systems course.

## 👨‍💻 Author

**Pouya Mirzaei**

- GitHub: [@pouya-mirzaei](https://github.com/pouya-mirzaei)

---

_Built with ❤️ for Operating Systems course_

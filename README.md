# WC-Tool

# File Chunk Reader and Processor

## Overview
This Python-based tool efficiently reads and processes large files in chunks. It calculates key file metrics such as total bytes, words, and characters, and allows users to specify desired metrics using command-line flags.

---

## Features
- Reads files in chunks to handle large files without memory exhaustion.
- Supports the following metrics:
  - **Bytes**: Total size of the file in bytes.
  - **Words**: Total number of words in the file.
  - **Characters**: Total number of characters in the file.
  - **Lines**: No. of lines
- Command-line flags to customize output:
  - `-b`: Display byte count.
  - `-w`: Display word count.
  - `-c`: Display character count.
  - `-l`: Display line count.
  - ``: Display all metrics (default behavior).
- Robust error handling for invalid file paths or missing arguments.

---

## Usage

### Prerequisites
- Python 3.7 or higher must be installed.

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-chunk-reader.git
   ```
2. Navigate to the project directory:
   ```bash
    cd file-chunk-reader
    ```
3. Run the script:
    ```bash
    python script.py <file_path> [flags]
    ```

### Why File Chunking?

 Memory Efficiency: 
- Processes large files without loading them entirely into memory.
- Scalability: Handles multi-GB files seamlessly.
- Performance: Maintains system responsiveness by processing data incrementally.

 Error Handling
- Missing File Path: Prompts the user to input a valid file.
- Invalid File Path: Displays "File not found" message.
- Empty Files: Handles gracefully without crashes.

Contributions are welcome! Fork this repository, make your changes, and submit a pull request.


## Contact
For questions or suggestions, feel free to reach out:

Email: charanpulivendula1999@gmail.com

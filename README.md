# 💾 Log Analyzer (Python)

This project is a simple but functional command-line utility developed in Python to parse and analyze large system log files. The primary goal is to demonstrate core Python programming skills relevant to data processing and system administration.

## 🛠️ Key Skills Demonstrated (Relevant to CV)

* **File Handling & I/O:** Efficiently reading external log files (`sample.log`).
* **String Manipulation:** Processing line-by-line data to identify specific keywords (INFO, WARNING, ERROR).
* **Basic Data Analysis:** Aggregating counts to generate a structured summary report.
* **Error & Exception Management:** Ensuring the script handles cases where the log file is not found.

## ⚙️ How It Works (`log_analyzer.py`)

The script reads the specified log file, iterates through each line, and uses simple string searching (case-insensitive) to categorize the entries into three levels: `INFO`, `WARNING`, and `ERROR`. It then prints a clear summary of the findings.

## 📊 Example Output

When run on the included `sample.log` file, the output is as follows:

--- Log Analysis Summary --- Total Lines Processed: 5 INFO (Information) Count: 2 WARNING (Warning) Count: 1 ERROR (Error) Count: 2

## 📝 Status

**Current Status:** Completed (Core functionality achieved).

**Future Improvements (WIP):**
* Implementing logging to a separate output file instead of standard output.
* Adding support for command-line arguments to specify the log file path.
* Integrating regular expressions (regex) for more complex pattern matching.

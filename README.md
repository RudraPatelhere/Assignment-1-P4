CPU-Performance-Analyzer
A Python script that measures execution time for sequential and parallel computing, retrieves CPU temperature, and prints system details.

📌 About This Project
This project:

Reads an Excel file containing user data.
Runs a sum of squares calculation in two ways:
Sequentially (single process).
In parallel (using 8 processes).
Measures execution time for both methods.
Fetches CPU temperature using LibreHardwareMonitor.
Displays system properties like OS, CPU model, and number of cores.
🛠 How to Use
1️⃣ Install Dependencies
Make sure you have Python and Conda installed, then run:

bash
Copy
Edit
conda create --name assignment1 python=3.8
conda activate assignment1
pip install -r requirements.txt
2️⃣ Setup LibreHardwareMonitor
Download LibreHardwareMonitor.
Extract LibreHardwareMonitorLib.dll and place it in the same folder as assignment1.py.
If needed, unblock the file (Right-click → Properties → Check "Unblock" → Apply).
3️⃣ Run the Script
bash
Copy
Edit
python assignment1.py
This will:
✅ Read and display Excel student info.
✅ Measure execution time for sequential and parallel computing.
✅ Display CPU temperature before and after execution.
✅ Print system details.

💡 Real-Life Applications
This project helps with:

Benchmarking – Compare execution time for single vs. multi-threaded tasks.
System Monitoring – Track CPU temperature under different loads.
Performance Optimization – Understand how parallel computing improves efficiency.

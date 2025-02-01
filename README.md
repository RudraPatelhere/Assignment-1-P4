CPU-Performance-Analyzer
Analyze system performance using Python – measures execution time for sequential and parallel computing, retrieves CPU temperature, and prints system details.

📌 About This Project
This Python project performs system performance analysis by:

Reading an Excel file containing user data.
Running a computational task (sum of squares) in two ways:
Sequentially (single process).
In parallel (using 8 processes).
Measuring execution time for both methods.
Fetching CPU temperature using LibreHardwareMonitor.
Displaying system properties like OS, CPU model, and number of cores.
🛠 How to Use
1️⃣ Install Dependencies
First, make sure you have Python and Conda installed, then set up the required environment:

bash
Copy
Edit
conda create --name assignment1 python=3.8
conda activate assignment1
pip install -r requirements.txt
2️⃣ Ensure You Have LibreHardwareMonitor
Download LibreHardwareMonitor from here.
Extract the LibreHardwareMonitorLib.dll and place it in the same directory as assignment1.py.
If you downloaded it, unblock the file (Right-click → Properties → Check "Unblock" → Apply).
3️⃣ Run the Script
bash
Copy
Edit
python assignment1.py
This will: ✔ Read and display Excel student info.
✔ Measure execution time for sequential and parallel computing.
✔ Display CPU temperature before and after execution.
✔ Print system details.

💡 Real-Life Applications
This project demonstrates performance measurement and system monitoring, which are important for: 🔹 Benchmarking – Compare execution time between single-threaded and multi-threaded computations.
🔹 System Monitoring – Track CPU temperature to analyze system health under load.
🔹 Optimizing Code – Understand the impact of parallel computing on performance.

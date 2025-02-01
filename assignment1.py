import time
import multiprocessing
import pandas as pd
import platform
import psutil
import os

def GET_CPU_TEMPERATURE():
    """
    Get CPU temperature using LibreHardwareMonitor via pythonnet.
    Requirements:
      - LibreHardwareMonitorLib.dll must be unblocked and in the same folder as this script.
      - pythonnet must be installed (pip install pythonnet).
      - May need Administrator rights on Windows.
    """
    try:
        import clr  # use pythonnet to call .NET code
    except ImportError:
        return "pythonnet is not installed"

    try:
        # Build the DLL path from the current folder
        DLL_PATH = os.path.join(os.getcwd(), "LibreHardwareMonitorLib.dll")
        if not os.path.exists(DLL_PATH):
            return "LibreHardwareMonitorLib.dll not found in the current directory"

        # Add the .NET assembly for LibreHardwareMonitor
        clr.AddReference(DLL_PATH)

        # Import necessary classes from the assembly
        from LibreHardwareMonitor.Hardware import Computer, SensorType

        # Create a computer object and enable CPU sensors
        COMPUTER_OBJ = Computer()
        COMPUTER_OBJ.IsCpuEnabled = True
        COMPUTER_OBJ.Open()

        CPU_TEMPS = []  # list to store temperature values
        # Loop through all hardware and get CPU temperatures
        for HARDWARE in COMPUTER_OBJ.Hardware:
            if str(HARDWARE.HardwareType).lower() == "cpu":
                HARDWARE.Update()
                for SENSOR in HARDWARE.Sensors:
                    if str(SENSOR.SensorType).lower() == "temperature" and SENSOR.Value is not None:
                        CPU_TEMPS.append(SENSOR.Value)

        if CPU_TEMPS:
            AVG_TEMP = sum(CPU_TEMPS) / len(CPU_TEMPS)  # average temperature
            return f"{AVG_TEMP:.1f}°C"
        else:
            return "No CPU temperature sensor data available"
    except Exception as E:
        return f"Error using LibreHardwareMonitor: {E}"

def SEQUENTIAL_CALCULATION():
    """
    Calculate the sum of squares from 0 to 999,999.
    """
    RESULT = 0  # start with zero
    for I in range(10**6):
        RESULT += I ** 2  # add square of I to RESULT
    return RESULT

def PARALLEL_CALCULATION(CHUNK):
    """
    Calculate the sum of squares for a range defined by CHUNK (start, end).
    """
    START, END = CHUNK  # unpack the range values
    RESULT = 0  # initialize RESULT to zero
    for I in range(START, END):
        RESULT += I ** 2  # add square of I
    return RESULT

def MAIN():
    # --- Part 1: Read and Print Excel File ---
    print("Reading excel file 'student_info.xlsx'...")
    try:
        DF = pd.read_excel("student_info.xlsx")  # read the Excel file
        print("Excel file content:")
        print(DF)
    except Exception as E:
        print("Error reading Excel file:", E)
    
    # --- Part 2: Print System Properties ---
    print("\nSystem Properties:")
    print("Platform:", platform.system())  # show the operating system
    print("Processor:", platform.processor())  # show the processor info
    print("Number of CPUs:", psutil.cpu_count(logical=True))  # show CPU count
    
    # --- Part 3: CPU Temperature Before Running Calculations ---
    print("\nCPU Temperature before calculations:", GET_CPU_TEMPERATURE())
    
    # --- Part 4: Sequential Calculation ---
    print("\nStarting sequential calculation...")
    SEQ_START_TIME = time.time()  # record start time
    SEQ_RESULT = SEQUENTIAL_CALCULATION()  # do sequential calc
    SEQ_ELAPSED_TIME = time.time() - SEQ_START_TIME  # calculate elapsed time
    print("Sequential calculation result:", SEQ_RESULT)
    print("Time taken for sequential run: {:.4f} seconds".format(SEQ_ELAPSED_TIME))
    print("CPU Temperature after sequential run:", GET_CPU_TEMPERATURE())
    
    # --- Part 5: Parallel Calculation Using Multiprocessing ---
    print("\nStarting parallel calculation using 8 processes...")
    TOTAL_ITERATIONS = 10**6  # total number of iterations
    NUM_PROCESSES = 8  # number of processes to use
    CHUNK_SIZE = TOTAL_ITERATIONS // NUM_PROCESSES  # iterations per process
    
    CHUNKS = []  # list to store ranges for each process
    for I in range(NUM_PROCESSES):
        START = I * CHUNK_SIZE
        END = (I + 1) * CHUNK_SIZE if I != NUM_PROCESSES - 1 else TOTAL_ITERATIONS
        CHUNKS.append((START, END))  # add the range tuple
    
    PAR_START_TIME = time.time()  # record start time for parallel calc
    with multiprocessing.Pool(processes=NUM_PROCESSES) as POOL:
        RESULTS = POOL.map(PARALLEL_CALCULATION, CHUNKS)  # perform calc in parallel
    PAR_ELAPSED_TIME = time.time() - PAR_START_TIME  # calculate elapsed time
    PAR_RESULT = sum(RESULTS)  # combine results from all processes
    
    print("Parallel calculation result:", PAR_RESULT)
    print("Time taken for parallel run: {:.4f} seconds".format(PAR_ELAPSED_TIME))
    print("CPU Temperature after parallel run:", GET_CPU_TEMPERATURE())

if __name__ == "__main__":
    MAIN()  # run the main function

import threading
import time
import math

# Function to calculate factorial
def calculate_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n}! calculated.")

# Function to measure total time for all 3 factorials using threads
def measure_time():
    # Record the start time before threads start
    start_time = time.perf_counter_ns()

    # Create three threads for factorial calculations
    t1 = threading.Thread(target=calculate_factorial, args=(50,))
    t2 = threading.Thread(target=calculate_factorial, args=(100,))
    t3 = threading.Thread(target=calculate_factorial, args=(200,))

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    # Record the end time after all threads have finished
    end_time = time.perf_counter_ns()

    # Calculate total time taken (in nanoseconds)
    time_elapsed = end_time - start_time
    return time_elapsed

# Run 10 rounds of testing
def main():
    rounds = 10
    times = []

    print("\n========== Multithreading Factorial Test ==========")
    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        total_time = measure_time()
        times.append(total_time)
        print(f"Total time for round {i}: {total_time} nanoseconds")

    # Calculate total and average time
    total_all_rounds = sum(times)
    average_time = total_all_rounds / len(times)

    print("\n===============================================")
    print("Summary of Execution Times (in nanoseconds):")
    for i, t in enumerate(times, 1):
        print(f"Round {i}: {t}")
    print("-----------------------------------------------")
    print(f"Total Time (All 10 Rounds): {total_all_rounds:.0f} nanoseconds")
    print(f"Average Time Taken: {average_time:.0f} nanoseconds")
    print("===============================================")

if __name__ == "__main__":
    main()

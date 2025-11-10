import time
import math

# Function to calculate factorial
def calculate_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n}! calculated.")
    return result

# Function to measure total time for sequential factorial calculation
def measure_time():
    # Use high-precision timer for better accuracy
    start_time = time.perf_counter_ns()

    # Perform factorials one by one (sequentially)
    calculate_factorial(50)
    calculate_factorial(100)
    calculate_factorial(200)

    end_time = time.perf_counter_ns()

    # Calculate total time taken in nanoseconds
    time_elapsed = end_time - start_time
    return time_elapsed

# Run 10 rounds of testing
def main():
    rounds = 10
    times = []

    print("\n========== Sequential Factorial Test (No Multithreading) ==========")
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

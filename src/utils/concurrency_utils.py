import concurrent.futures
from typing import Callable, List
from ..models.concurrent_execution_result import ConcurrentExecutionResult
import time



def execute_concurrent_tasks(task_func: Callable, task_args: List, timeout: int, max_workers: int):
    start_time = time.time()  # Start the timer
    results = []
    total_requests = 0
    error_requests = 0
    durations = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        try:
            future_to_task = {executor.submit(task_func, arg): arg for arg in task_args}
            for future in concurrent.futures.as_completed(future_to_task, timeout=timeout):
                result = future.result()
                results.append(result)
                total_requests += 1
                durations.append(result['duration'])
                if result["status"] == "failed":
                    error_requests += 1
        except KeyboardInterrupt:
            print("Process interrupted by user.")
        except concurrent.futures.TimeoutError:
            print("Process timed out.")

    total_time = time.time() - start_time  # Calculate total time

    return ConcurrentExecutionResult(results, total_requests, error_requests, durations, total_time)

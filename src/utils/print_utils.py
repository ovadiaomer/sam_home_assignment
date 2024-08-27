def print_execution_summary(execution_result):
    print("Test is over!")
    print(f"Total time: {execution_result.total_time:.2f} seconds")
    print(f"Requests in total: {execution_result.total_requests}")
    print(f"Error rate: {execution_result.error_rate():.2f}% ({execution_result.error_requests} / {execution_result.total_requests})")
    print(f"Average time for one request: {execution_result.average_time():.4f} seconds")
    print(f"Max time for one request: {execution_result.max_time():.4f} seconds")
    print(f"P90 time for requests: {execution_result.p90_time():.4f} seconds")

import csv
from ..models.api_response import ApiResponse

def save_results_to_csv(file_path, execution_result):
    """
    Save the results of the stress test to a CSV file.

    :param file_path: Path to the CSV file.
    :param execution_result: An instance of ConcurrentExecutionResult containing the results.
    """
    with open(file_path, "w", newline="") as csvfile:
        fieldnames = ["domain", "status", "duration", "response"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in execution_result.results:
            # Convert the dictionary to an ApiResponse instance
            api_response = ApiResponse(
                domain=result['domain'],
                status=result['status'],
                duration=result['duration'],
                response=result['response']
            )
            writer.writerow(api_response.to_dict())

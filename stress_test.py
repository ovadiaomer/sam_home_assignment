import requests
import time
from random import sample
from src.utils.api_utils import ApiUtils
from src.models.api_response import ApiResponse
from src.utils.concurrency_utils import execute_concurrent_tasks
from src.utils.print_utils import print_execution_summary
from src.utils.csv_utils import save_results_to_csv
from src.utils.arg_utils import parse_arguments
from src.constants import POPULAR_DOMAINS, API_URL, HEADERS

def query_domain(domain):
    """
        Queries the reputation service for a specific domain and returns the result.

        :param domain: The domain to query.
        :return: A dictionary representing the API response.
        """
    start_time = time.time()
    try:
        response = ApiUtils(API_URL.format(domain), HEADERS).get()
        duration = time.time() - start_time

        # Create a success ApiResponse object
        api_response = ApiResponse.from_success(domain, duration, response)

    except requests.RequestException as e:
        duration = time.time() - start_time
        # Create a failure ApiResponse object
        api_response = ApiResponse.from_failure(domain, duration, str(e))

    # Return the ApiResponse object converted to a dictionary
    return api_response.to_dict()


def stress_test(domains, num_concurrent_requests, timeout):
    # Use the utility function to execute the tasks concurrently
    execution_result = execute_concurrent_tasks(
        task_func=query_domain,
        task_args=domains,
        timeout=timeout,
        max_workers=num_concurrent_requests
    )

    print_execution_summary(execution_result)
    save_results_to_csv("stress_test_results.csv", execution_result)


def run_stress_test():
    args = parse_arguments()
    domains_to_test = sample(POPULAR_DOMAINS, args.num_domains)
    # Running the stress test
    stress_test(domains_to_test, args.concurrent_requests, args.timeout)


if __name__ == "__main__":
    run_stress_test()

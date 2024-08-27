# Reputation Service Stress Test

## Overview

This CLI tool is designed to simulate stress on a Reputation service by sending multiple concurrent requests to an API endpoint. It supports customization of the number of domains, the number of concurrent requests, and the timeout for the entire operation. The tool collects and reports metrics such as total requests, error rate, average response time, max response time, and the 90th percentile response time.

## Features

- **Concurrency**: Supports multiple concurrent requests.
- **Customizable**: Allows configuration of the number of domains, concurrent requests, and timeout.
- **Error Handling**: Handles request errors and user interruptions (e.g., `KeyboardInterrupt`).
- **Results**: Provides a summary of the stress test and saves detailed results in a CSV file.

## Requirements

- Python 3.x
- `requests` library
- `concurrent.futures` (part of the Python standard library)

## Installation

1. **Clone the repository** (or extract the provided ZIP file):
   ```bash
   git clone https://github.com/ovadiaomer/sam_home_assignment
   cd reputation-stress-test
   
## Set up a virtual environment 

   python3 -m venv reputation-stress-env
   

## Activate the virtual environment (mac):
   source reputation-stress-env/bin/activate
## Activate the virtual environment (win):
   .\reputation-stress-env\Scripts\activate

## Install the dependencies:
pip install -r requirements.txt

## Usage
python stress_test.py -n <number_of_domains> -c <concurrent_requests> -t <timeout_in_seconds>

## Example
   
   python stress_test.py --num_domains 500 --concurrent_
   requests 100 --timeout 120


## Results:
Results will be available under reputation-stress-env/stress_test_results.csv

## Example results:
Test is over!

Total time: 5.14 seconds

Requests in total: 500

Error rate: 0.00% (0 / 500)

Average time for one request: 0.3849 seconds

Max time for one request: 0.8043 seconds

P90 time for requests: 0.4659 seconds

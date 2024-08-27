from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(description="Reputation Service Stress Test CLI")
    parser.add_argument("-n", "--num_domains", type=int, default=5000, help="Number of domains to run (max: 5000)")
    parser.add_argument("-c", "--concurrent_requests", type=int, default=10, help="Number of concurrent requests")
    parser.add_argument("-t", "--timeout", type=int, default=60, help="Timeout in seconds for the stress test")
    return parser.parse_args()

#!/usr/bin/env python3
print("Starting execute script")
from parsl.executors.high_throughput.process_worker_pool import execute_task
from parsl.serialize import serialize

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,
                        help="Input pickle file")
    parser.add_argument("-o", "--output", required=True,
                        help="Output pickle file")
    args = parser.parse_args()

    print(f"Input : {args.input}")
    print(f"Output : {args.output}")

    result = None
    with open(args.input, 'rb') as f:
        fn_buf = f.read()
        print("Read input pkl file")
        try:
            result = execute_task(fn_buf)
            print("Finished execution")
        except Exception as e:
            print(f"Execution failed due to {e}")
            result = e
    result_buf = serialize(result)
    with open(args.output, 'wb') as f:
        f.write(result_buf)

    
    

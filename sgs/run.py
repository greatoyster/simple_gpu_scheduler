import multiprocessing
import os
import argparse


def single_gpu_multiple_tasks(commands, num_pgpus, num_vgpus, gpu_ids):
    if gpu_ids == None:
        gpu_ids = [i for i in range(num_pgpus)]
    else:
        gpu_ids = [
            id
            for part in gpu_ids.split(",")
            for id in (
                range(int(part.split("-")[0]), int(part.split("-")[-1]) + 1)
                if "-" in part
                else [int(part)]
            )
        ]
        num_pgpus = len(gpu_ids)
    num_vgpus = num_pgpus if num_vgpus == -1 else num_vgpus

    # Assign GPUs based on the number of GPUs specified
    gpu_assignments = [f"export CUDA_VISIBLE_DEVICES={i}" for i in gpu_ids]
    # Store the created processes
    processes = []
    for i in range(num_vgpus):
        # Distribute tasks to each GPU in a round-robin manner
        process_tasks = commands[i::num_vgpus]
        # Combine the GPU assignment command and the task command to form the complete command to be executed
        process_cmd = " && ".join([gpu_assignments[i % num_pgpus]] + process_tasks)
        print(process_cmd)
        # Create a process and assign it the task of executing the command
        process = multiprocessing.Process(target=os.system, args=(process_cmd,))
        processes.append(process)
    # Start all processes
    for p in processes:
        p.start()
    # Wait for all processes to complete
    for p in processes:
        p.join()


def _create_parser():
    parser = argparse.ArgumentParser(description="Run commands on multiple GPUs.")
    parser.add_argument(
        "-f", "--commands", type=str, required=True, help="Path to command file."
    )
    gpu_group = parser.add_mutually_exclusive_group(required=True)
    gpu_group.add_argument(
        "-p", "--num_pgpus", type=int, help="Number of physical GPUs to use."
    )
    gpu_group.add_argument(
        "-g",
        "--gpu_ids",
        type=str,
        help="Comma-separated list of GPU IDs to use (e.g., '0,1,2'). Use '-' to specify ranges (e.g., '0,2-4,7' is equivalent to '0,2,3,4,7').",
    )
    parser.add_argument(
        "-v", "--num_vgpus", type=int, default=-1, help="Number of virtual GPUs to use."
    )
    return parser


if __name__ == "__main__":
    parser = _create_parser()
    args = parser.parse_args()
    print(args)
    with open(args.commands, "r") as f:
        commands = [line.strip() for line in f.readlines()]
    single_gpu_multiple_tasks(commands, args.num_pgpus, args.num_vgpus, args.gpu_ids)

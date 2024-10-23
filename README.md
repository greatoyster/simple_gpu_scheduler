# simple_gpu_scheduler
This is a simple tool that helps you effectively utilize multiple GPUs to run tasks.

# installation
```
git clone https://github.com/greatoyster/simple_gpu_scheduler.git && cd simple_gpu_scheduler && pip install .
```
or
```
pip install sgs@git+https://github.com/greatoyster/simple_gpu_scheduler.git
```

# usage
```
usage: run.py [-h] -f COMMANDS (-p NUM_PGPUS | -g GPU_IDS) [-v NUM_VGPUS]

Run commands on multiple GPUs.

options:
  -h, --help            show this help message and exit
  -f COMMANDS, --commands COMMANDS
                        Path to command file.
  -p NUM_PGPUS, --num_pgpus NUM_PGPUS
                        Number of physical GPUs to use.
  -g GPU_IDS, --gpu_ids GPU_IDS
                        Comma-separated list of GPU IDs to use (e.g., '0,1,2'). Use '-' to specify ranges (e.g., '0,2-4,7' is equivalent to '0,2,3,4,7').
  -v NUM_VGPUS, --num_vgpus NUM_VGPUS
                        Number of virtual GPUs to use.
```

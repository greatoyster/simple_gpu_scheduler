# simple_gpu_scheduler
This is a simple tool that helps you effectively utilize multiple GPUs to run tasks.

# installation
```
git clone https://github.com/greatoyster/simple_gpu_scheduler.git && cd simple_gpu_scheduler && pip install .
```

# usage
```
python -m sgs.run [-h] -f COMMANDS [-p NUM_PGPUS] [-v NUM_VGPUS]

Run commands on multiple GPUs.

options:
  -h, --help            show this help message and exit
  -f COMMANDS, --commands COMMANDS
                        Path to command file.
  -p NUM_PGPUS, --num_pgpus NUM_PGPUS
                        Number of physical GPUs to use.
  -v NUM_VGPUS, --num_vgpus NUM_VGPUS
                        Number of virtual GPUs to use.
```
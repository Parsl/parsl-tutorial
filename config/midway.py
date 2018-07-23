from libsubmit.channels import SSHChannel
from libsubmit.providers import SlurmProvider

from parsl.config import Config
from parsl.executors.ipp import IPyParallelExecutor
from parsl.executors.ipp_controller import Controller

config = Config(
    executors=[
        IPyParallelExecutor(
            provider=SlurmProvider(
                'westmere',
                init_blocks=1,
                min_blocks=1,
                max_blocks=2,
                nodes_per_block=1,
                tasks_per_node=4,
                parallelism=0.5,
                overrides='''module load mvapich2;
module load python/3.5.2+gcc-4.8;
source /scratch/midway/yadunand/parsl_env_3.5.2_gcc/bin/activate'''
            ),
            label='midway_ipp'
        )
    ]
)

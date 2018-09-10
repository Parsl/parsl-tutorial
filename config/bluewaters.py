from libsubmit.channels import LocalChannel
from libsubmit.launchers import AprunLauncher
from libsubmit.providers import TorqueProvider

from parsl.config import Config
from parsl.executors.ipp import IPyParallelExecutor
from parsl.executors.ipp_controller import Controller

from parsl.data_provider.scheme import GlobusScheme

config = Config(
    executors=[
        IPyParallelExecutor(
            label='bw_ipp',
            provider=TorqueProvider(
                channel=LocalChannel(),
                nodes_per_block=1,
                tasks_per_node=1,
                init_blocks=1,
                min_blocks=1,
                max_blocks=1,
                launcher=AprunLauncher(overrides="-b -- bwpy-environ --"),
                overrides='''#PBS -l nodes=1:ppn=32 
module load bwpy''',
                walltime='00:30:00'

            ),
            controller=Controller(public_ip="10.0.0.146"),
            working_dir="/tmp",
            storage_access=[GlobusScheme(
                endpoint_uuid="d59900ef-6d04-11e5-ba46-22000b92c6ec",
                endpoint_path="/",
                local_path="/"
            )]
        )

    ],
)

import parsl
from parsl.channels import LocalChannel
from parsl.launchers import AprunLauncher
from parsl.providers import TorqueProvider

from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname

from parsl.data_provider.scheme import GlobusScheme

config = Config(
    executors=[
        HighThroughputExecutor(
            label="bluewaters_htex",
            worker_debug=True,
            address="<LOGIN_NODE>",
            provider=TorqueProvider(
                channel=LocalChannel(),
                init_blocks=1,
                max_blocks=1,
                min_blocks=1,
                nodes_per_block=1,
                launcher=AprunLauncher(overrides="-b -- bwpy-environ --"),
                scheduler_options='''#PBS -l nodes=1:ppn=32
#PBS -q debug''',
                worker_init='''module load bwpy''',
                walltime='00:30:00'
            ),
            storage_access=[GlobusScheme(
                endpoint_uuid="d59900ef-6d04-11e5-ba46-22000b92c6ec",
                endpoint_path="/",
                local_path="/"
            )]
        )

    ],
)
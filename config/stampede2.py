from parsl.config import Config

from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname

from parsl.data_provider.scheme import GlobusScheme

config = Config(
    executors=[
        HighThroughputExecutor(
            label="s2_htex",
            worker_debug=True,
            address=address_by_hostname(),
            provider=SlurmProvider(
                channel=LocalChannel(),
                nodes_per_block=1,
                init_blocks=1,
                min_blocks=1,
                max_blocks=1,
                partition='skx-normal',
                scheduler_options='''#SBATCH -A Parsl-Eval''',
                worker_init='''source activate parsl-test''',
                walltime='00:30:00'
            ),
            storage_access=[GlobusScheme(
                endpoint_uuid="ceea5ca0-89a9-11e7-a97f-22000a92523b",
                endpoint_path="/",
                local_path="/"
            )]
        )

    ],
)
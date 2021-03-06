from pytorch_lightning.plugins.training_type.ddp import DDPPlugin
from pytorch_lightning.plugins.training_type.ddp2 import DDP2Plugin
from pytorch_lightning.plugins.training_type.ddp_spawn import DDPSpawnPlugin
from pytorch_lightning.plugins.training_type.dp import DataParallelPlugin
from pytorch_lightning.plugins.training_type.horovod import HorovodPlugin
from pytorch_lightning.plugins.training_type.parallel import ParallelPlugin
from pytorch_lightning.plugins.training_type.rpc import RPCPlugin
from pytorch_lightning.plugins.training_type.rpc_sequential import RPCSequentialPlugin
from pytorch_lightning.plugins.training_type.sharded import DDPShardedPlugin
from pytorch_lightning.plugins.training_type.sharded_spawn import DDPSpawnShardedPlugin
from pytorch_lightning.plugins.training_type.single_device import SingleDevicePlugin
from pytorch_lightning.plugins.training_type.single_tpu import SingleTPUPlugin
from pytorch_lightning.plugins.training_type.tpu_spawn import TPUSpawnPlugin
from pytorch_lightning.plugins.training_type.training_type_plugin import TrainingTypePlugin

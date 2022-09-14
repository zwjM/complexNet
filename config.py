"""
  这是一个用于存储全局配置的属性的文件
"""

import torch
import numpy as np

INIT_SEED = 0
np.random.seed(INIT_SEED)
torch.manual_seed(INIT_SEED)
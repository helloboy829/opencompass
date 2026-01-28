from mmengine.config import read_base

with read_base():
    # 导入SuperGPQA数据集配置
    from opencompass.configs.datasets.supergpqa.supergpqa_gen import supergpqa_datasets
    # 导入您的自定义模型配置
    from opencompass.configs.models.custom.qwen332_custom import models

# 配置数据集和模型
datasets = supergpqa_datasets

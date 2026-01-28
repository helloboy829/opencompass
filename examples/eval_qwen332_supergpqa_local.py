from opencompass.models import OpenAI
from opencompass.datasets.supergpqa.supergpqa import (
    SuperGPQADataset,
    SuperGPQAEvaluator,
)
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
import os

# ========== 模型配置 ==========
api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
)

models = [
    dict(
        abbr='qwen332-local',
        type=OpenAI,
        path='qwen332',  # 修改为您的模型名称
        key='EMPTY',  # 本地模型不需要 API key
        openai_api_base='http://10.147.75.115:1025/v1/chat/completions',  # 修改为您的本地 API 地址
        meta_template=api_meta_template,
        query_per_second=2,  # 根据您的服务器性能调整
        max_out_len=2048,
        max_seq_len=4096,
        batch_size=8,
        retry=3,
        temperature=0.7,
    ),
]

# ========== 数据集配置 ==========
# 获取项目根目录（opencompass 目录）
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据集相对路径：data/supergpqa_custom.jsonl
dataset_path = os.path.join(project_root, 'data', 'supergpqa_custom.jsonl')

reader_cfg = dict(
    input_columns=[
        'question',
        'options',
        'discipline',
        'field',
        'subfield',
        'difficulty',
        'infer_prompt',
        'prompt_mode',
    ],
    output_column='answer_letter',
)

infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(
                    role='HUMAN',
                    prompt='{infer_prompt}',
                ),
            ],
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer),
)

eval_cfg = dict(
    evaluator=dict(type=SuperGPQAEvaluator),
    pred_role='BOT',
)

datasets = [
    dict(
        type=SuperGPQADataset,
        abbr='supergpqa_custom',
        path='json',
        data_files={'train': dataset_path},  # 使用相对路径
        prompt_mode='zero-shot',
        reader_cfg=reader_cfg,
        infer_cfg=infer_cfg,
        eval_cfg=eval_cfg,
    )
]

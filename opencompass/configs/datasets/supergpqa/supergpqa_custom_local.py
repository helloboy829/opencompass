from opencompass.datasets.supergpqa.supergpqa import (
    SuperGPQADataset,
    SuperGPQAEvaluator,
)
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever


# Reader configuration
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

# Inference configuration
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

# Evaluation configuration
eval_cfg = dict(
    evaluator=dict(type=SuperGPQAEvaluator),
    pred_role='BOT',
)

supergpqa_custom_dataset = dict(
    type=SuperGPQADataset,
    abbr='supergpqa_custom',
    # 使用本地 JSONL 文件
    path='json',  # 使用 datasets 库的 json 加载器
    data_files={'train': 'd:/code1/opencompass/data/supergpqa_custom.jsonl'},  # 指定为 train split
    prompt_mode='zero-shot',
    reader_cfg=reader_cfg,
    infer_cfg=infer_cfg,
    eval_cfg=eval_cfg,
)

supergpqa_datasets = [supergpqa_custom_dataset]

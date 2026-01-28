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
    # 修改这里：使用您自己的数据集路径
    # 选项1：使用本地JSON/JSONL文件
    path='d:/code1/opencompass/data/supergpqa_custom.jsonl',
    # 选项2：使用HuggingFace数据集（默认）
    # path='m-a-p/SuperGPQA',
    prompt_mode='zero-shot',
    reader_cfg=reader_cfg,
    infer_cfg=infer_cfg,
    eval_cfg=eval_cfg,
)

supergpqa_datasets = [supergpqa_custom_dataset]

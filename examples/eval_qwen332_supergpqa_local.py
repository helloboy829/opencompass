from opencompass.models import OpenAI
from opencompass.datasets.supergpqa.supergpqa import (
    SuperGPQADataset,
    SuperGPQAEvaluator,
)
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever

# ========== 模型配置 ==========
api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
)

models = [
    dict(
        abbr='qwen-plus-custom',
        type=OpenAI,
        path='qwen-plus',
        key='sk-5364d7c0e0424965beecf6b677a3bfb4',
        openai_api_base='https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions',
        meta_template=api_meta_template,
        query_per_second=2,
        max_out_len=2048,
        max_seq_len=4096,
        batch_size=8,
        retry=3,
        temperature=0.7,
    ),
]

# ========== 数据集配置 ==========
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
        data_files={'train': 'd:/code1/opencompass/data/supergpqa_custom.jsonl'},
        prompt_mode='zero-shot',
        reader_cfg=reader_cfg,
        infer_cfg=infer_cfg,
        eval_cfg=eval_cfg,
    )
]

from opencompass.models import OpenAI

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
        path='qwen-plus',  # 对应您API中的model参数
        key='sk-5364d7c0e0424965beecf6b677a3bfb4',  # 如果不需要API key，设置为EMPTY；如果需要，设置实际的key
        openai_api_base='https://dashscope.aliyuncs.com/compatible-mode/v1',  # 您的API地址
        meta_template=api_meta_template,
        query_per_second=2,  # 根据您的API限流调整
        max_out_len=2048,
        max_seq_len=4096,
        batch_size=8,
        retry=3,
        temperature=0.7,
    ),
]

# models = [
#     dict(
#         abbr='qwen332-custom',
#         type=OpenAI,
#         path='qwen332',  # 对应您API中的model参数
#         key='EMPTY',  # 如果不需要API key，设置为EMPTY；如果需要，设置实际的key
#         openai_api_base='http://10.147.75.115:1025/v1/chat/completions',  # 您的API地址
#         meta_template=api_meta_template,
#         query_per_second=2,  # 根据您的API限流调整
#         max_out_len=2048,
#         max_seq_len=4096,
#         batch_size=8,
#         retry=3,
#         temperature=0.7,
#     ),
# ]
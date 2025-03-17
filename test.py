from llmx import llm
from llmx.datamodel import TextGenerationConfig

messages = [
    {"role": "user", "content": "Capital of India?"}
]


def test_case():
    openrouter_gen = llm(provider="openrouter")
    config = TextGenerationConfig(model="qwen/qwen-2.5-72b-instruct:free",max_tokens=500)
    openrouter_response = openrouter_gen.generate(messages, config=config)
    answer = openrouter_response.text[0].content
    print(answer)
    return ("delhi" in answer.lower())
print(test_case())
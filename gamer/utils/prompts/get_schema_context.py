def get_schema_context_prompt(query: str):

    schema_context_prompt = (f"""

"""
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{schema_context_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages
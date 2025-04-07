import os
from litellm import completion
from config.logging import logger

class LlmClient:
    def __init__(self):
        pass

    async def get_response(self, chat_history):
        try:
            # Call OpenRouter's completion API
            response = completion(
                model="openrouter/meta-llama/llama-4-maverick:free",
                messages=chat_history
            )
            logger.info(f"Response from LLM: {response}")
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            #todo handle exception
            print(f"Error in generating response: {e}")

llm_client = LlmClient()
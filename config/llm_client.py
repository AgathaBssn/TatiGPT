import os
from litellm import completion
from config.logging import logger

# Set the OpenRouter API key
os.environ["OPENROUTER_API_KEY"] = "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"

class LlmClient:
    def __init__(self):
        pass

    async def get_response(self, chat_history):
        logger.info(f"Response from LLM: {chat_history}")
        try:
            # Call OpenRouter's completion API
            response = completion(
                model="openrouter/meta-llama/llama-4-maverick:free",
                messages=chat_history
            )
            logger.info(f"Response from LLM: {response}")
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            #to do handle exception
            print(f"Error in generating response: {e}")

llm_client = LlmClient()
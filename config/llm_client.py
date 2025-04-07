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
            return "I'm sorry, I couldn't process your request."

llm_client = LlmClient()
import os
import requests
from together import Together

class LlmClient:
    def __init__(self):
        self.client = Together()

    def get_response(self, user_input: str):
        # Vérification pour s'assurer que user_input est une chaîne de caractères valide
        if not isinstance(user_input, str) or not user_input.strip():
            raise ValueError("Le contenu de l'entrée utilisateur doit être une chaîne de caractères non vide.")

        # Ajout du champ "type" dans le message
        messages = [
            {"role": "user", "content": user_input, "type": "text"}
        ]
        
        # Création de la demande de complétion
        stream = self.client.chat.completions.create(
            model="meta-llama/Llama-Vision-Free",
            messages=messages,
            stream=True
        )

        response_content = ""
        for chunk in stream:
            response_content += chunk.choices[0].delta.content or ""

        return response_content

# Usage example
llm_client = LlmClient()


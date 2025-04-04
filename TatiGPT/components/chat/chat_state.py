import reflex as rx

from config.llm_client import llm_client
from config.logging import logger


class ChatState(rx.State):
    chat_history: list[dict[str, str]] = []

    current_user_input: str = ""

    @rx.event
    def set_current_user_input(self, value: str):
        self.current_user_input = value

    @rx.event
    def clear_chat_history(self):
        self.chat_history = []

    @rx.event
    async def on_load(self):
        logger.info("ChatState loaded")
        self.clear_chat_history()

    @rx.event
    async def handle_user_input(self):
        # Ajouter la question de l'utilisateur à l'historique
        self.chat_history.append({"question": self.current_user_input, "answer": ""})
        # Réinitialiser le champ d'entrée de l'utilisateur
        self.current_user_input = ""

        # Passer uniquement la question de l'utilisateur (et non un message complet)
        response = llm_client.get_response(self.chat_history[-1]["question"])
        
        # Afficher la réponse dans l'historique du chat
        logger.info(f"Response: {response}")
        # Supposons que la réponse est directement la chaîne de texte de l'IA
        self.chat_history[-1]["answer"] = response

        # Logguer l'historique du chat après la réponse
        logger.info(f"Chat history: {self.chat_history}")

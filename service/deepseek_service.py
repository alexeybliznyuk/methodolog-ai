from repository.deepseek_repository import DeepSeekRepository

class DeepSeekService:
    def __init__(self):
        self.repository = DeepSeekRepository()

    def generate_structure(self, user_input):
        system_prompt = "Предложи структуру курса по этому опроснику."
        conversation = [{"role": "system", "content": f"{system_prompt}"}]
        conversation += user_input

        data = {
            "model": "deepseek-chat",
            "messages": conversation
        }

        response = self.repository.call_deepseek_api(data)
        return response
from models.llm_model import ChatLLM
from utils.preprocessing import clean_input

llm = ChatLLM(model_name="gpt2")  # You can change to "gpt2-medium" for ~345M params

def get_response(user_input):
    cleaned = clean_input(user_input)
    return llm.generate_response(cleaned)

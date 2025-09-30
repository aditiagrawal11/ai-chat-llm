from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

class ChatLLM:
    def __init__(self, model_name="gpt2", max_length=512, temperature=0.7, top_p=0.9):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            pad_token_id=self.tokenizer.eos_token_id
        )

    def generate_response(self, prompt):
        outputs = self.generator(prompt, num_return_sequences=1)
        return outputs[0]["generated_text"]

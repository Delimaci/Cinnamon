from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Load the pre-trained GPT-Neo 125M model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"

# Initialize the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name)

# Set the pad_token to eos_token for GPT-Neo
tokenizer.pad_token = tokenizer.eos_token

def generate_response(user_input):
    # Define a conversational prompt for Cinnamon
    prompt = """
    I am Cinnamon, a friendly and playful AI. I always respond with warmth and enthusiasm, like a friendly companion. My goal is to engage the user in a fun and casual conversation. Be responsive, lighthearted, and welcoming.
    
    User: {user_input}
    Cinnamon: 
    """
    
    # Format the prompt with the user's input
    formatted_prompt = prompt.format(user_input=user_input)

    # Encode the formatted prompt into tokens and create attention mask
    inputs = tokenizer(formatted_prompt, return_tensors='pt', padding=True, truncation=True)

    # Generate a response using the model with specific settings for more focused output
    output = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],  # Explicit attention mask
        max_length=100,  # Keep responses shorter and more to the point
        num_return_sequences=1,  # Only one response
        num_beams=1,  # Using greedy search to keep responses direct
        no_repeat_ngram_size=2,  # Prevent repetition in the response
        do_sample=True,  # Enable sampling for some level of variability
        temperature=0.7,  # Control randomness (slightly higher for more variety)
        top_p=0.7,  # Nucleus sampling with some randomness
        top_k=50,  # Limits sampling to the top 50 tokens
        pad_token_id=tokenizer.eos_token_id,  # Use eos token for padding
        early_stopping=True  # Stop when a coherent response is generated
    )

    # Decode the generated tokens to a string
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Return the model's response, removing the input part from the response
    response = response[len(formatted_prompt):].strip()

    return response

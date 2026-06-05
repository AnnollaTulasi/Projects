from langchain.chat_models import init_chat_model
GEMINI_API_KEY = "AQ.Ab8RN6Ix2PvWc75-3Z782b7UyQvmLyYY331Ek_t8bGkjEvBJNA"
model = init_chat_model(model="gemini-3-flash-preview" ,
                        model_provider="google-genai" ,
                        api_key = GEMINI_API_KEY
                        )
response = model.invoke("is pen better than a pencil?")
response_str = response.content[0]["text"]
print(response_str)
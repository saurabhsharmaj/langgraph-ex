from langchain_core.language_models.fake_chat_models import FakeMessagesListChatModel
from langchain_core.messages import AIMessage

# Create a fake model that always returns the same response
model = FakeMessagesListChatModel(
    responses=[
        AIMessage(content="Hello from Mock LLM!")
    ]
)

# Invoke the model
response = model.invoke("Hi")

# Print the response
print(response.content)
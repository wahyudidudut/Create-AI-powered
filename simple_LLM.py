import os
from langchain_openai import ChatOpenAI

# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["OPENAI_API_KEY"] = "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"

# Mendefinisikan jenis model 
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

text = "Berikan fakta menarik tentang dudut!"
print(gpt3.invoke(text).content)
import os

API_OPENAI:str = "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"
API_ANTHROPIC:str = "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"
API_HF:str = "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"
API_VERTEX_PROJECT:str = "recital-gpu"
API_VERTEX_LOCATION:str = "europe-west9"
API_ALEPH_ALPHA:str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNDAwOCwidG9rZW5faWQiOjQzNTV9.5Gw5gOS8idS3L9HUueMnfUwf9M08vEgZ5Mg-nPBaCHw"
API_MISTRAL:str ="RNvgjkGSfkW2qJ34PzqFlij52mPgPSQI"
API_COHERE:str = "gNZeA88hqIPlFX2Reuag9nIqeE4NETTt3n0kUi6T"

os.environ["OPENAI_API_KEY"] = API_OPENAI
os.environ["ANTHROPIC_API_KEY"] = API_ANTHROPIC
os.environ["HUGGINGFACE_API_KEY"] = API_HF
os.environ["VERTEX_PROJECT"] = API_VERTEX_PROJECT
os.environ["VERTEX_LOCATION"] = API_VERTEX_LOCATION
os.environ['ALEPHALPHA_API_KEY'] = API_ALEPH_ALPHA
os.environ['MISTRAL_API_KEY'] = API_MISTRAL
os.environ["COHERE_API_KEY"] = API_COHERE

# if neededd run the command below for Google models
# os.system('gcloud config set project recital-gpu')
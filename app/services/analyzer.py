from transformers import pipeline 

# LOAD MODEL 
analyzer = pipeline("text-classification", model="huggingface/transformers")

# EXAMPLE 
user_input = "Je suis très fatigué et démotivé au travail."
result = analyzer(user_input)

# PREDICTIONS 
print(result)

"""
NOTA BENE 
Pour personnaliser le modèle : le fine-tuner sur un dataset avec Hugging Face
- soit on crée le jeu de données 
soit on en trv un public ex: """
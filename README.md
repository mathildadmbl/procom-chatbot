# procom-chatbot

        chatbot-burnout/
        ├── app/
        
        │   ├── main.py           # Fichier principal pour FastAPI
        
        │   ├── routers/          # Pour diviser les routes si le projet s'agrandit
        │   │   └── chat.py       # Route dédiée à la gestion des messages
        │   ├── services/         # Logique métier et intégrations (OpenAI, Hugging Face)
        │   │   └── chatgpt.py    # Intégration avec ChatGPT
        │   │   └── analyzer.py   # Analyse des réponses utilisateur
        │   ├── utils/            # Fonctions utilitaires
        │   │   └── report.py     # Génération de rapports
        │   └── models/           # Modèles de données (Pydantic)
        │       └── user_input.py # Schéma pour les requêtes utilisateurs
        ├── requirements.txt      # Dépendances Python
        ├── Dockerfile            # Fichier Docker pour le déploiement
        ├── .env                  # Clés d’API et variables d’environnement
        ├── tests/                # Tests unitaires
        │   └── test_chat.py
        ├── README.md             # Documentation du projet
        └── data/                 # (Optionnel) Fichiers de données ou logs

from gensim import models
DEFAULT_ACCESS_URL = "http://www.chatbot.hk/Robot.Mark1.api.ph"
DEFAULT_ACCESS_TOKEN = "63ebdad609d02ac15a71bde64fb21f8ea43ac513"
CUSTOM_ACCESS_URL = "https://voice-kit-v2-demo.firebaseio.com"
MODLES = models.Word2Vec.load('word2vec.model')
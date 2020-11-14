# Pharmaceutical-Assistance-Chatbot-PharmaBot
This Repository is dedicated to <Strong>PharmaBot</Strong>, a ChatBot that provides information about medication and medicine mainly in Morocco.

It's a ChatBot interacting in English, based on Natural Language Processing (NLP), programmed in Python and deployed on Messenger.
Its mission is to respond to the informational need of the user in the pharmaceutical field, <Strong>PharmaBot</Strong> can answers questions relating to medicines available mainly on the Moroccan market
and possibly other medications.

It may specify, at the user's request, the adverse effects of an the precautions to be taken when using a certain medicine, the precautions to be taken when using a certain The information provided is based on the drug product, its selling price or reimbursement rate.

The data for this ChatBot are extracted from the open drug database published on the Moroccan government's open data portal:

www.data.gov.ma

The conversational data on which the ChatBot relies on to respond to the user is extracted from a Dataset available on GitHub at the following address:

https://github.com/Bhargava-Sai-P/Chatbot-using-nltk/blob/master/dialog_talk_agent.xlsx

The main libraries and Frameworks used for this project are:
- NLTK (Natural Language Toolkit) for tokenizing, chunking and extracting entities from the user input.
- Scikit-Learn to perform word embedding bag of words model and count vectorizer model.
- Flask to deploy the chatbot on facebook apps and messenger.
- Ngrok For tunneling.

![General Schema](https://github.com/Youtir/Pharmaceutical-Assistance-Chatbot-PharmaBot/blob/master/generalSchema.png)

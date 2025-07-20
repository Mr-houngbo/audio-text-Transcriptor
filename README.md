# 🔊 Transcripteur Audio ↔ Texte
Ce projet Python permet :
- la **conversion de texte en audio** (synthèse vocale via `pyttsx3`)
- la **lecture vocale de fichiers PDF**
- la **transcription d’audio en texte** (reconnaissance vocale avec `speech_recognition` et `pyaudio`)
---
## 🚀 Fonctionnalités
- 🔁 Conversion texte <--> audio
- 📄 Lecture à haute voix d’un fichier PDF
- 🎙️ Reconnaissance vocale du micro et affichage du texte
---
## 🛠️ Installation
Clonez le dépôt et installez les dépendances :
```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo
pip install -r requirements.txt
```
---
## ▶️ Utilisation
### 🔉 Texte vers audio
```python
# Synthèse vocale simple
droid.say("Hello, my name is Gord.")
```
### 📚 Lecture d’un PDF à voix haute
Décommentez les lignes dans la section PDF et placez votre fichier `doc.pdf` dans le dossier.

### 🧠 Audio vers texte (via le micro)
```python
# Le programme écoute votre voix et affiche le texte reconnu
print("Parlez maintenant...")
```
---
## 📦 Dépendances
Voir le fichier [`requirements.txt`](requirements.txt)
---
## 🧑‍💻 Auteur
Projet réalisé par **Mr-houngbo** 🤖
---
## 📄 Licence
Ce projet est sous licence MIT.

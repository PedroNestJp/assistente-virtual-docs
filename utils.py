# utils.py
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
import spacy
from transformers import pipeline
from gtts import gTTS

# Carregar o modelo de linguagem do spaCy
nlp = spacy.load("en_core_web_sm")

# Função para extrair texto de arquivos PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "".join(page.extract_text() for page in pdf.pages)
    return text

# Função para extrair texto de arquivos Word
def extract_text_from_word(file_path):
    doc = Document(file_path)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    return text

# Função para extrair texto de imagens usando OCR
def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text

# Função para validar e interpretar o texto extraindo palavras-chave
def validate_and_interpret_text(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# Configuração do modelo de sumarização do Hugging Face Transformers
summarizer = pipeline("summarization")

# Função para resumir o texto
def summarize_text(text, max_length=150, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Função para converter texto para áudio usando gTTS
def convert_text_to_audio(text, output_path="summary_audio.mp3"):
    tts = gTTS(text, lang='pt-br')
    tts.save(output_path)
    return output_path

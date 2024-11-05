# main.py
from utils import (
    extract_text_from_pdf,
    extract_text_from_word,
    extract_text_from_image,
    validate_and_interpret_text,
    summarize_text,
    convert_text_to_audio,
)

def main():
    print("Bem-vindo ao Assistente Virtual de Documentos!")
    print("Escolha o tipo de documento para análise: PDF, Word ou imagem.")
    file_type = input("Digite o tipo de documento (pdf/word/image): ").strip().lower()
    file_path = input("Digite o caminho completo do arquivo: ").strip()

    # Extração de texto de acordo com o tipo de documento
    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    elif file_type == "word":
        text = extract_text_from_word(file_path)
    elif file_type == "image":
        text = extract_text_from_image(file_path)
    else:
        print("Tipo de arquivo não suportado. Por favor, escolha pdf, word ou image.")
        return

    print("\nTexto Extraído do Documento:")
    print(text)

    # Validação e Interpretação
    print("\nProcessando palavras-chave e interpretação...")
    keywords = validate_and_interpret_text(text)
    print(f"Palavras-chave identificadas: {keywords}")

    # Resumo do conteúdo
    print("\nGerando resumo do documento...")
    summary = summarize_text(text)
    print(f"Resumo: {summary}")

    # Converter Resumo em Áudio
    print("\nConvertendo resumo para áudio...")
    audio_path = convert_text_to_audio(summary)
    print(f"Áudio salvo em: {audio_path}")
    print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    main()

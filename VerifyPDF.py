import PyPDF2
import sys

def test_pdf_vulnerability(pdf_file):
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Ici, vous pouvez ajouter des tests spécifiques pour vérifier la vulnérabilité
            print(f"Le fichier {pdf_file} a été analysé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'analyse du fichier {pdf_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ScriptPDF.py <fichier_pdf>")
        sys.exit(1)

    test_pdf_vulnerability(sys.argv[1])
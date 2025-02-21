import sys

def check_pdf_for_js(pdf_file):
    try:
        with open(pdf_file, "rb") as f:
            pdf_content = f.read()
            if b"/JavaScript" in pdf_content:
                print("JavaScript trouvé dans le PDF.")
            else:
                print("Aucun JavaScript trouvé dans le PDF.")

    except Exception as e:
        print(f"Erreur lors de l'analyse du fichier {pdf_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez fournir le nom du fichier PDF en paramètre.")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    check_pdf_for_js(pdf_file)
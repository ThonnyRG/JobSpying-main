import json
import os
import typst

class CoverLetterGenerator:
    def __init__(self, json_path: str = os.path.join("documents", "cover_letter.json"), 
                 template_path: str = os.path.join("templates", "cover_letter", "cover_letter.typ"), 
                 output_dir: str = "documents"):
        self.json_path = json_path
        self.template_path = template_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_pdf(self):
        # 1. Validar existencia de cover_letter.json
        if not os.path.exists(self.json_path):
            print(f"Error: El archivo '{self.json_path}' no existe.")
            return

        # 2. Leer los datos exactamente como están en el JSON
        with open(self.json_path, 'r', encoding='utf-8') as f:
            cover_data = json.load(f)

        company_slug = cover_data.get("company_name", "Company").replace(" ", "_")
        output_pdf_path = os.path.join(self.output_dir, f"Cover_Letter_{company_slug}.pdf")

        # 3. Compilar usando Typst
        try:
            typst.compile(
                self.template_path, 
                output=output_pdf_path, 
                sys_inputs={"data": json.dumps(cover_data)}
            )
            print(f"Carta de presentación generada con éxito: {output_pdf_path}")
        except Exception as e:
            print(f"Error al compilar con Typst: {e}")


if __name__ == '__main__':
    generator = CoverLetterGenerator()
    generator.generate_pdf()
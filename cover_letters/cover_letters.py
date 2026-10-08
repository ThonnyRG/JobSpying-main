import json
import os
import sys

from fpdf import FPDF
from PIL import Image

MARGIN = 12.7  # mm = 0.5 in, igual que tu diseño
REQUIRED_KEYS = ["user_name", "company_name", "paragraphs"]


def clean(text: str) -> str:
    """Las fuentes estándar del PDF solo aceptan latin-1: normaliza comillas y guiones."""
    replacements = {
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-", "\u2026": "...", "\u2022": "-", "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.encode("latin-1", "replace").decode("latin-1")


def scaled_height(path: str, width: float) -> float:
    with Image.open(path) as im:
        w, h = im.size
    return width * h / w


class CoverLetterGenerator(FPDF):
    def __init__(self, data: dict, images_dir: str = os.path.join("templates", "src"),
                 font_size: float = 12):
        missing = [k for k in REQUIRED_KEYS if k not in data]
        if missing:
            raise KeyError(f"Faltan claves en cover_letter.json: {', '.join(missing)}")

        super().__init__(orientation="P", unit="mm", format="Letter")
        self.data = data
        self.images_dir = images_dir
        self.body_size = font_size

        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.set_auto_page_break(True, margin=MARGIN)
        self.set_title(f'{data["user_name"]} - Cover Letter - {data["company_name"]}')
        self.set_author(data["user_name"])

    # ---------- utilidades ----------
    @property
    def content_width(self) -> float:
        return self.w - 2 * MARGIN

    @staticmethod
    def _lh(size: float) -> float:
        """Altura de línea en mm para un tamaño en pt."""
        return size * 0.3528 * 1.3

    def _img(self, name: str):
        path = os.path.join(self.images_dir, name)
        if not os.path.exists(path):
            print(f"Aviso: no se encontró {path}")
            return None
        return path

    def _text(self, text, size, style="", color=(0, 0, 0)):
        self.set_font("Helvetica", style, size)
        self.set_text_color(*color)
        self.multi_cell(0, self._lh(size), clean(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    # ---------- secciones ----------
    def _header(self):
        top = MARGIN
        banner_w = self.content_width * 0.67
        contact_w = self.content_width * 0.33
        banner_h = contact_h = 0

        banner = self._img("image2.png")
        if banner:
            banner_h = scaled_height(banner, banner_w)
            self.image(banner, x=MARGIN, y=top, w=banner_w)

        contact = self._img("image3.png")
        if contact:
            contact_h = scaled_height(contact, contact_w)
            self.image(contact, x=MARGIN + banner_w, y=top, w=contact_w)

        # Destinatario debajo del banner
        self.set_xy(MARGIN, top + banner_h + 1)
        self._text("To:", self.body_size, "B", color=(102, 102, 102))
        self._text(self.data["company_name"], 14, "B")
        self._text("Human Resources Manager", 14, "B")

        # Baja hasta el final del bloque de contacto si es más alto
        self.set_y(max(self.get_y(), top + contact_h) + 1)

    def _divider(self):
        path = self._img("image1.png")
        y = self.get_y()
        if path:
            h = scaled_height(path, self.content_width)
            self.image(path, x=MARGIN, y=y, w=self.content_width)
            self.set_y(y + h)
        else:
            self.line(MARGIN, y + 2, self.w - MARGIN, y + 2)
            self.set_y(y + 4)

    def _signature(self):
        path = self._img("image4.png")
        if not path:
            return
        sig_w = 45
        sig_h = scaled_height(path, sig_w)
        if self.get_y() + sig_h > self.h - MARGIN:
            self.add_page()
        self.image(path, x=MARGIN, y=self.get_y() + 1, w=sig_w)
        self.set_y(self.get_y() + sig_h + 1)

    # ---------- construcción ----------
    def build(self):
        size = self.body_size
        gap = self._lh(size) * 0.6

        self.add_page()
        self._header()
        self._divider()
        self.ln(3)

        self._text(f'Dear {self.data.get("hr_name", "Hiring Manager")},', size)
        self.ln(gap)
        for paragraph in self.data["paragraphs"]:
            self._text(paragraph, size)
            self.ln(gap)
        self._text("Thank you for your consideration.", size)

        self.ln(2)
        self._divider()
        self.ln(4)

        self._text("Sincerely,", size)
        self._text(self.data["user_name"], size)
        self._signature()
        return self


def render(data: dict, images_dir: str, output_dir: str = "documents",
           max_pages: int = 1, start_size: float = 12, min_size: float = 10):
    os.makedirs(output_dir, exist_ok=True)
    name = data["user_name"].replace(" ", "_")
    company = data["company_name"].replace(" ", "_")
    path = os.path.join(output_dir, f"CoverLetter_{name}_{company}.pdf")

    size = start_size
    while size >= min_size:
        pdf = CoverLetterGenerator(data, images_dir, font_size=size).build()
        if pdf.page_no() <= max_pages:
            pdf.output(path)
            print(f"Carta generada ({pdf.page_no()} pág, fuente: {size}pt): {path}")
            return path
        size -= 0.5

    print(f"No cabe en {max_pages} página a {min_size}pt. Acorta los párrafos.")
    return None


if __name__ == "__main__":
    letter_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join("documents", "cover_letter.json")
    with open(letter_file, encoding="utf-8") as f:
        letter_data = json.load(f)

    render(letter_data, images_dir=os.path.join("templates", "src"))
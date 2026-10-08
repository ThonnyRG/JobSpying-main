from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
import os
import json
class Generator:
    def __init__(self, data: dict, output_dir: str = "documents"):
        self.data = data
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def render_pdfs(self, max_pages: int = 1, start_size: float = 10, min_size: float = 9):
        slug = self.data.get("user_name", "CV").replace(" ", "_")
        path = os.path.join(self.output_dir, f"CV_{slug}.pdf")

        size = start_size
        while size >= min_size:
            pages = build_cv(self.data, path, size=size)
            if pages <= max_pages:
                print(f"CV generado ({pages} pág, fuente: {size}pt).")
                return
            size -= 0.5

        print(f"El contenido no cabe en {max_pages} página(s) a {min_size}pt. "
              "Recorta contenido o permite 2 páginas (max_pages=2).")



def build_cv(data, path, size=9.5):
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=size, leading=size * 1.25)
    bold = ParagraphStyle("bold", parent=body, fontName="Helvetica-Bold")
    h1 = ParagraphStyle("h1", parent=bold, fontSize=15, leading=18)
    h2 = ParagraphStyle("h2", parent=bold, fontSize=10.5, spaceBefore=8, spaceAfter=3)

    p = lambda t, s=body: Paragraph(escape(t), s)
    s = []
    s.append(p(data["user_name"], h1))
    s.append(p(f'{data["user_location"]} | {data["user_email"]} | {data["user_number"]} | {data["user_linkedin"]}'))

    if data.get("summary"):
        s += [p("SUMMARY", h2), p(data["summary"])]

    s.append(p("WORK EXPERIENCE", h2))
    for e in data["experiences"]:
        s.append(p(f'{e["company_name"]} - {e["role"]}', bold))
        s.append(p(f'{e["start_date"]} - {e["end_date"]} | {e["location"]}'))
        s.append(ListFlowable([ListItem(p(b), leftIndent=12) for b in e["description"]],
                              bulletType="bullet", start="•", leftIndent=12))
        s.append(Spacer(1, 4))

    s.append(p("SKILLS", h2))
    for label, key in [("Languages", "languages_list"), ("Backend & Frameworks", "back_and_frm_list"),
                       ("Databases & Systems", "cloud_and_system_list"), ("Tools & Practices", "data_and_tooling")]:
        s.append(Paragraph(f"<b>{escape(label)}:</b> {escape(data[key])}", body))

    s.append(p("EDUCATION", h2))
    for ed in data["education_list"]:
        s.append(p(f'{ed["institution"]} - {ed["degree"]}', bold))
        s.append(p(f'{ed["dates"]} | {ed["location"]}'))

    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=1.5*cm, rightMargin=1.5*cm,
                            topMargin=1.2*cm, bottomMargin=1.2*cm,
                            title=f'{data["user_name"]} - Software Engineer CV', author=data["user_name"])
    doc.build(s)
    return doc.page

if __name__ == "__main__":
    with open(os.path.join("documents", "resume.json"), encoding="utf-8") as f:
        info = json.load(f)
    Generator(info).render_pdfs(max_pages=2)
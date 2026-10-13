import os
from ats_check.ats_check import ATSScorer
from ats_check.resume_parser import ResumeParser
from ats_check.domain_classifier import DomainClassifier
from ats_check.skill_extractor import SkillExtractor

def evaluate_resume(file_path: str):
    # 1. Determinar la extensión del archivo
    _, file_ext = os.path.splitext(file_path)
    file_ext = file_ext.lower()

    if file_ext not in ['.pdf', '.docx']:
        print("Formato no soportado")
        return

    print(f"Analizando el archivo: {file_path} ...")

    # 2. Parsear el archivo (con soporte OCR automático si es PDF escaneado)
    parser = ResumeParser()
    parsed_data = parser.parse(file_path, file_ext)

    # 3. Extraer habilidades
    skill_extractor = SkillExtractor()
    skills = skill_extractor.extract(parsed_data['raw_text'])

    # 4. Clasificar el dominio o industria
    domain_classifier = DomainClassifier()
    domain = domain_classifier.classify(parsed_data['raw_text'], skills)

    # 5. Calcular puntuación ATS y generar reporte de diagnóstico
    scorer = ATSScorer()
    analysis_result = scorer.calculate_score(
        parsed_data=parsed_data,
        skills=skills,
        domain=domain,
        parsing_method=parsed_data['parsing_method'],
        ocr_confidence=parsed_data['ocr_confidence']
    )

    # 6. Mostrar resultados en consola
    print("\n" + "="*40)
    print(f"Analisys results for: {os.path.basename(file_path)}")
    print("="*40)
    print(f"ATS SCORE          : {analysis_result['score']} / 100")
    print(f"Category           : {analysis_result['category']}")
    print(f"Detected Domain    : {domain.primary} ({int(domain.confidence * 100)}% confidence)")
    print(f"Extraction Method  : {parsed_data['parsing_method']}")

    print("\nIssues:")
    if analysis_result['issues']:
        for issue in analysis_result['issues']:
            print(f" - [{issue.severity}] {issue.description}: {issue.suggestion}")
    else:
        print(" ¡Nothing found! Your document is in great shape.")

    print("\nSuggestions for Improvement:")
    for suggestion in analysis_result['suggestions'][:3]:
        print(f" - [{suggestion.category}] {suggestion.title}: {suggestion.description}")

    print("="*40)

if __name__ == '__main__':
    # Ejemplo de uso apuntando a uno de tus PDFs generados en documents/
    target_pdf = os.path.join("documents", "CV_Jesús_Antonio_Morales_Cruz.pdf")
    evaluate_resume(target_pdf)
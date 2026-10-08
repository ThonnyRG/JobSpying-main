import json
import pandas as pd
from openai import OpenAI

# 1. Configura tu API Key de OpenAI
client = OpenAI(api_key="TU_API_KEY_AQUI")

# 2. Define tu Perfil Profesional / Curriculum
MI_PERFIL = """
Soy Desarrollador de Software Jr con 1 año de experiencia en Python, Django y FastAPI.
Tengo conocimientos en bases de datos PostgreSQL y control de versiones con Git.
Busco roles Remote o en México.
Nivel de inglés: B2 (intermedio-avanzado).
"""


def evaluar_compatibilidad(descripcion_vacante, titulo_vacante):
    """Envía la descripción de la vacante al LLM para calcular el porcentaje de match."""
    if not descripcion_vacante or pd.isna(descripcion_vacante):
        return {"match_score": 0, "razon": "Sin descripción disponible"}

    prompt = f"""
    Evalúa qué tan compatible es el siguiente candidato con la oferta laboral.
    
    PERFIL DEL CANDIDATO:
    {MI_PERFIL}
    
    VACANTE ({titulo_vacante}):
    {descripcion_vacante[:2000]} # Limitamos texto para ahorrar tokens
    
    Responde ÚNICAMENTE en formato JSON estricto con la siguiente estructura:
    {{
        "match_score": <número del 0 al 100>,
        "razon": "<explicación breve de 1 o 2 oraciones de por qué hace o no match>"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Modelo económico y rápido
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.2,
        )

        resultado = json.loads(response.choices[0].message.content)
        return resultado
    except Exception as e:
        return {"match_score": 0, "razon": f"Error evaluando: {str(e)}"}


# 3. Iterar sobre las vacantes encontradas por JobSpy (limitamos a las primeras 10 para probar)
vacantes_a_evaluar = jobs.head(10).copy()

scores = []
razones = []

print("Analizando compatibilidad con las vacantes...")

for index, row in vacantes_a_evaluar.iterrows():
    evaluacion = evaluar_compatibilidad(row.get("description"), row.get("title"))
    scores.append(evaluacion.get("match_score", 0))
    razones.append(evaluacion.get("razon", ""))

# 4. Agregar los resultados al DataFrame y ordenar
vacantes_a_evaluar["match_score"] = scores
vacantes_a_evaluar["match_razon"] = razones

# Ordenar por las mejores vacantes
vacantes_filtradas = vacantes_a_evaluar.sort_values(
    by="match_score", ascending=False
)

# Guardar solo las que superen el 70% de compatibilidad
mejores_vacantes = vacantes_filtradas[vacantes_filtradas["match_score"] >= 70]
mejores_vacantes.to_csv("mejores_vacantes.csv", index=False)

# Mostrar resultados principales
mejores_vacantes[["title", "company", "match_score", "match_razon", "job_url"]]
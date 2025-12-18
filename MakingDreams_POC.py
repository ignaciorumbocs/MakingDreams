# --- IMPLEMENTACIÓN DE LA PRUEBA DE CONCEPTO (POC) ---
# Este código está diseñado para ejecutarse en un entorno de Jupyter Notebook.
# Instalación requerida: !pip install -U -q google-generativeai

import google.generativeai as genai
import json
import time

# 1. Configuración de Seguridad y API
# La clave de API se deja vacía para ser configurada en el entorno de ejecución.
apiKey = "" 
genai.configure(api_key=apiKey)

def interior_design_ai_assistant(room, style, budget, specifics):
    """
    Función principal que implementa técnicas de Fast Prompting.
    Optimiza el uso de la API realizando una única consulta para obtener múltiples resultados.
    """
    
    # Selección del modelo compatible con el entorno
    model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
    
    # DEFINICIÓN DEL SYSTEM PROMPT (Técnicas: Role Prompting + Few-Shot)
    system_message = """
    Eres un Consultor Senior de Diseño de Interiores. Tu tarea es ayudar a personas con poco presupuesto a profesionalizar sus espacios.
    
    REGLAS DE RESPUESTA:
    1. Analiza el presupuesto y el estilo antes de responder.
    2. Proporciona un plan de acción de 3 pasos.
    3. Genera un prompt para IA de imagen en INGLÉS que sea fotorrealista.
    4. Responde EXCLUSIVAMENTE en formato JSON.

    EJEMPLO DE FORMATO:
    {
      "analisis": "Razonamiento del diseño basado en el presupuesto...",
      "pasos_accion": ["paso 1", "paso 2", "paso 3"],
      "image_prompt": "Professional interior photography of [Style] [Room], 8k, cinematic lighting, photorealistic..."
    }
    """

    # INPUT DEL USUARIO (Técnica: Delimitadores)
    user_prompt = f"""
    DATOS DEL PROYECTO:
    - HABITACIÓN: {room}
    - ESTILO: {style}
    - PRESUPUESTO: {budget}
    - DETALLES ESPECÍFICOS: {specifics}
    """

    # Implementación de Backoff Exponencial para manejo de errores de API
    retries = [1, 2, 4, 8]
    for wait_time in retries:
        try:
            response = model.generate_content(
                contents=[{"parts": [{"text": user_prompt}]}],
                system_instruction={"parts": [{"text": system_message}]},
                generation_config={"response_mime_type": "application/json"}
            )
            return json.loads(response.text)
        except Exception:
            time.sleep(wait_time)
            
    return {"error": "No se pudo obtener respuesta de la API."}

# --- ÁREA DE PRUEBAS ---
if __name__ == "__main__":
    # Simulación de entrada de usuario
    mi_habitacion = "Sala de estar pequeña"
    mi_estilo = "Boho Chic"
    mi_presupuesto = "150 USD"
    mis_detalles = "Mucha luz de ventana, quiero usar plantas y madera"

    print("🚀 Procesando propuesta de diseño...")
    resultado = interior_design_ai_assistant(mi_habitacion, mi_estilo, mi_presupuesto, mis_detalles)

    if "error" not in resultado:
        print("\n🏠 ANÁLISIS DEL EXPERTO:")
        print(resultado['analisis'])
        
        print("\n🛠️ PASOS A SEGUIR:")
        for i, paso in enumerate(resultado['pasos_accion'], 1):
            print(f"{i}. {paso}")
            
        print("\n🖼️ PROMPT PARA GENERADOR DE IMAGEN (Copia esto en Nightcafe):")
        print(resultado['image_prompt'])
    else:
        print(f"❌ Error: {resultado['error']}")

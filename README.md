MakingDreams: Asistente Inteligente de Diseño y Visualización

1. Introducción

Presentación del Problema

El diseño de interiores suele ser un proceso costoso y difícil de visualizar para personas sin formación técnica. Los usuarios enfrentan dos problemas principales:

Falta de lenguaje técnico: No saben cómo describir lo que quieren de forma que un experto lo entienda.

Incertidumbre visual: Tienen miedo de realizar cambios físicos sin ver una representación realista previa.

Propuesta de Solución

Desarrollamos una herramienta basada en Fast Prompting que actúa como un "Traductor de Sueños a Diseño". El usuario ingresa datos simples y la IA devuelve un plan de acción estructurado y un prompt técnico optimizado para generadores de imagen resolviendo la brecha entre la idea y la ejecución.

2. Metodología

Para lograr una solución rentable y eficiente, implementaremos el siguiente procedimiento:

Extracción de Variables: Se definen inputs clave.

Prompting Estructurado: Utilizaremos la técnica de System Role y Few-Shot Prompting para asegurar que la IA mantenga un tono profesional y un formato de salida consistente.

Optimización de Consultas: En lugar de hacer varias llamadas a la API, utilizaremos un único prompt complejo que genere tanto el asesoramiento como el prompt de imagen en un solo bloque (JSON), reduciendo los costos de latencia y tokens.

3. Herramientas y Tecnologías

Modelo de Texto: Gemini 2.5 Flash.

Técnicas de Prompting:

Role Prompting: Definimos a la IA como un "Senior Interior Designer".

Chain-of-Thought : Pedimos a la IA que razone los pasos del diseño antes de dar el prompt final.

Few-Shot: Proporcionamos un ejemplo de buena salida para garantizar el formato.

Generación de Imagen: Recomendamos el uso de Nightcafe utilizando el prompt técnico genera

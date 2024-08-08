meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "GG": "Expresion de orgullo, o suerte",
            "XD": "Algo inesperado que da risa, / emoji muriendo de risa, / o algo chistoso",
            "NOOB": "Palabra de origen americano, forma de decir a una persona novato",
            "PRO": "Persona habilidosa en un area especifica de algun juego, tema, etc",
            "MANCO": "Persona muy mala en videojuegos molestosa"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Error tipografico, o no se encuentra la palabra")

    

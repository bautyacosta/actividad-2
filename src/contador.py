import re

def cuenta(descriptions):
    charla_count = 0
    entretenimiento_count = 0
    musica_count = 0

    for description in descriptions:
        desc = description.lower()

        if re.search(r'\bcharla\b', desc):
            charla_count += 1
        if re.search(r'\bentretenimiento\b', desc):
            entretenimiento_count += 1
        if re.search(r'\bmúsica\b', desc):  # con tilde
            musica_count += 1

    print(f"charla: {charla_count}, entretenimiento: {entretenimiento_count}, música: {musica_count}")

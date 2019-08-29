import pampo

pt_news = """
Manifestar
"""

response = pampo.extract_entities(pt_news)

print("\n".join(response))

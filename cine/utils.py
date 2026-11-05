def formato_clp(valor):
 """Convierte 4500 en '$4.500' (pesos chilenos, sin decimales)."""
 return "$" + f"{int(valor):,}".replace(",", ".")

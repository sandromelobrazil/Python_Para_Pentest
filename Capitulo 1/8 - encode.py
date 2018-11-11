nome = "Daniel Moreno"

codificado = nome.encode("base64")
decodificado = codificado.decode("base64")

print nome, "codificado em base64:", codificado
print codificado, "decodificado em base64:", decodificado
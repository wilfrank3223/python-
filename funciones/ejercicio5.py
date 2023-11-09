def compra(marca,cantidad,valor):
    return dict(
    marca=marca,
    cantidad=cantidad,
    valor=valor*cantidad

)

print(f' lo comprado fue:{compra(marca=“AMD",cantidad=3,valor=2500000)}')
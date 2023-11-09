def compra(marca,cantidad,valor):
    return dict(
    marca=marca,
    cantidad=cantidad,
    valor=valor*cantidad

)

print(f' lo comprado fue:{compra("AMD",3,2500000)}')
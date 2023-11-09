def compra(marca,cantidad,valor=5000):
    return dict(          
    marca=marca,
    cantidad=cantidad,
    valor=valor*cantidad

)

print(f' lo comprado fue:{compra("RYZEN")}')
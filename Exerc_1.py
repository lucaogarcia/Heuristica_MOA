# Definir o custo total, o quanto foi pago e o troco

custo = 1000.00
pagamento = 1007.73
troco = pagamento - custo

cedula = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

for n in range(len(cedula)):
    numero_cedulas = 0
    while True:
        if troco > 0 and cedula[n] <= troco:
            troco -= cedula[n]
            numero_cedulas += 1
        else:
            break
    print(f"{numero_cedulas} cédulas de {cedula[n]}")
        

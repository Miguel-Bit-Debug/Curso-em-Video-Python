medida=float(input('Uma distancia em metros: '))
km= medida*0.001
hm= medida*0.01
dam= medida*0.1
cm= medida*100
mm=medida*1000
print('A medida de {}m corresponde a'.format(medida))
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{:.1f} dam'.format(dam))
print('{} cm'.format(cm))
print('{} mm'.format(mm))
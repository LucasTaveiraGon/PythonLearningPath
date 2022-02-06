larg = float(input('Digite a largura da parede a ser pintada: '))
alt = float(input('Digite a altura da parede a ser pintada: '))
area = larg * alt
tinta = area*2
print('sua parede tem as dimensões de {} x {} e sua area é de {}m²'
      'e você ira precisar de {}L de tinta ' .format(larg, alt, area, tinta))
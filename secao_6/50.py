ano=0
chico=1.50
ze=1.10
while ze<chico:
    chico+=0.02
    ze+=0.03
    ano+=1
print(f'demorou {ano} ano(s), para Ze ficar crescer até {ze:.2f}m e chico {chico:.2f}m.')
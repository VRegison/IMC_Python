#IMC
nome = input('Digite seu nome :');
altura = input('Digite sua Altura :');
peso = input('Digite seu Peso :');

imc = float(peso) / (float(altura) * float(altura))

if imc <= 18.5 :
   print(imc)
   print("IMC :" +  str(round(imc,2))  + " - Abaixo do peso normal");
   
elif imc <= 24.9 and imc >= 18.9 :
   print("IMC: "+  str(round(imc,2))  +" - Peso normal");

elif imc <= 28.9 and imc >= 25 :
   print("IMC: "+ str(round(imc,2)) +" - Excesso de peso");
   
elif imc <=34.9  and imc >= 30 :
   print("IMC: "+ str(round(imc,2)) +" - Obesidade classe 1");

elif imc <=39.9  and imc >= 35 :
   print("IMC: "+  str(round(imc,2))  +" - Obesidade classe 2");
   
elif imc >=40 :
   print("IMC: "+  str(round(imc,2))  +" - Obesidade classe 3");
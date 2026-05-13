archivo=open(".\\Archivos\\log.txt","a", encoding="utf-8")
texto=input("Ingrese una frase: ")
edad=int(input("Ingresa tu edad: "))
estatura=float(input("Ingrese su estatura: "))
archivo.write(texto+"\n")
#archivo.write(f"{edad}\n")
archivo.write(str(edad)+"\n")
archivo.write(str(estatura)+"\n")

              
archivo.close()
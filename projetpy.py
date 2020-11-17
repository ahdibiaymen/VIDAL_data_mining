import re,urllib.request,sys 
print("ERREUR NOMBRES D'ARGUMENT PASSES",len(sys.argv)-1)
if len(sys.argv)==1: 
	print("ERREUR AUCUN ARGUMENT PASSE")
else:
	if not(len(sys.argv)==2):
		print("ERREUR NOMBRE ARGUMENT DEPASSE LA LIMITE ,RESPECTEZ LA FORME A-Z")
	else:
		if not(sys.argv[1][1]=='-') or sys.argv[1][0].upper()>sys.argv[1][2].upper():
			print("ERREUR FORME INCORRECTE ,RESPECTEZ LA FORME A-Z")
		else:
			if not(sys.argv[1][0].upper().isalpha()) or not(sys.argv[1][2].upper().isalpha()):
				print("ERREUR LES ARGUMENTS PASSES NE SONT PAS DES CARACTERES,RESPECTEZ LA FORME A-Z")
			else:
				if not(len(sys.argv[1])==3):
					print("ERREUR LES ARGUMENTS SONT DES CHAINES DE CARACTERES,RESPECTEZ LA FORME A-Z")
				else:
					nbtot=0
					var3=open('infos.txt','w',encoding='utf-16-le')   
					var2=open('subst.dic','w',encoding='utf-16-le')
					var2.write("\ufeff")#BOM 
					for i in range(ord(sys.argv[1][0].upper()),ord(sys.argv[1][2].upper())+1):
						nbsb=0
						page =urllib.request.urlopen("https://www.vidal.fr/Sommaires/Substances-"+chr(i)+".htm")
						htmlcontent=page.read().decode('utf-8')
						r=re.findall("Substance/(.+)\.htm\">(.+?)<",htmlcontent)
						print("ASPIRATION DE MEDICAMENTS SUBSTANCE \\"+chr(i)+"/ ....")
						for j in r:
							nbsb+=1
							nbtot+=1
							var2.write(j[1]+",.N+subst\n")
						var3.write("nombre substance de la lettre \\"+chr(i)+"/:"+str(nbsb)+"\n") 
					var2.close()
					var3.write("LE NOMBRE TOTAL DES SUBSTANCE = "+str(nbtot))
					var3.close()
print("FIN DE PROGRAMME")    
 
import re,sys
print("ENRICHISSEMENT DE DICTIONNAIRE A PARTIR DE CORPUS_MEDICAL ...")
if not(len(sys.argv)==2):
	print("ERREUR D'ARGUMENT")
else:
	if not(sys.argv[1]=="corpus-medical.txt"):
		print("ERREUR NOM FICHIER INCORRECT")
	else:	
		var=open('corpus-medical.txt','r',encoding='utf-8').readlines()
		var2=open('subst.dic','a',encoding='utf-16-le')
		var3=open('subst_enri.dic','w',encoding='utf-16-le')
		var3.write("\ufeff")
		cpt=1
		for i in var:
			c=re.findall("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml|µg|µl|gr|g|l).+",i,re.I)
			for j in c:
				var2.write(j[0]+",.N+subst\n")
				var3.write(j[0]+",.N+subst\n")
		var3.close()		
		print("AFFICHAGE DES MEDICAMENTS ISSUS DE L'ENRICHISSEMENT ")	
		var3=open('subst_enri.dic','r',encoding='utf-16-le').readlines()
		for i in var3:
			c=re.findall("(\w+),(.+)",i,re.I)
			for x in c:
				print(str(cpt)+":"+x[0])
			cpt+=1
		var2.close()
		print("SUPPRESSION DES DOUBLANTS DE SUBST.DIC...")
		var2=open('subst.dic','r',encoding='utf-16-le').readlines()
		var4=open('subst.dic','w',encoding='utf-16-le')
		for i in list(set(i.lower() for i in var2)):
			var4.write(i)
		print("FAIT!")
		var4.close()
		print("TRI DE SUBST.DIC....")
		var2=open('subst.dic','r',encoding='utf-16-le').readlines()
		var4=open('subst.dic','w',encoding='utf-16-le')
		var4.write("\ufeff")#BOM
		for i in sorted(var2,key=lambda s: s.lower()):
			var4.write(i)	
		print("FAIT!")	
		var4.close()
		
print("FIN PROGRAMME ENRICHISSEMENT")


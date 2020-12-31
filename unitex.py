import os,shutil
#add UnitexToolLogger to your  environment variables in your machine Or ..
#Change Unitex_path variable to the location of "UnitexToolLogger" folder in your machine 
Unitex_path="d:\\Users\\Asus\\AppData\\Local\\Unitex-GramLab\\App\\UnitexToolLogger" 
Unitex_ressources="d:\\Users\\Asus\\AppData\\Local\\Unitex-GramLab\\French"
os.system("rd /s corpus-medical_snt")
if os.path.exists("corpus-medical_snt"):
    shutil.rmtree("corpus-medical_snt") 
os.mkdir("corpus-medical_snt")
os.system(f"{Unitex_path} Normalize corpus-medical.txt -r Norm.txt")
os.system(f"{Unitex_path} Tokenize corpus-medical.txt -a Alphabet.txt")
os.system(f"{Unitex_path} Compress subst.dic")
os.system(f"{Unitex_path} Dico -t corpus-medical.snt -a Alphabet.txt subst.bin")
os.system(f"{Unitex_path} Grf2Fst2 projetpy.grf")
os.system(f"{Unitex_path} Locate -t corpus-medical.snt projetpy.fst2 -a Alphabet.txt -L -I --all")
os.system(f"{Unitex_path} Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")


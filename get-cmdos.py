#This file is an assistant for install/update/uninstall CmdOS
#Warning, this assistant can only update CmdOS v2.3 and ulterior version to the latest version

import os
import urllib.request
import zipfile
import shutil
import sys
import requests as req

language=input("Choisissez un langage / Chose your language : fr / en : ")
if language=="fr":
    chose=input("Voulez vous installer (i), désinstaller (d) ou mettre à jour CmdOS (m) : ")
    if chose=="i":
        path=input("Veullier indiquer le répertoire où vous voulez installer CmdOS (il doit être vide) : ")
        print("Vérification du répertoire...")
        if os.path.exists(path)==True and os.listdir(path)==[]:
            print("Récupération des fichiers...")
            filename, headers = urllib.request.urlretrieve("https://github.com/lolo859/CmdOS/archive/refs/heads/main.zip", filename=path+"/CmdOS.zip")
            print("Dépaquetage en cours...")
            with zipfile.ZipFile(path+"/CmdOS.zip","r") as zipref:
                zipref.extractall(path)
            os.remove(path+"/CmdOS.zip")
            list_file=os.listdir(path+"/CmdOS-main")
            for file in list_file:
                print("Déplacement du fichier "+file+" depuis "+path+"/CmdOS-main/"+file+" vers "+path)
                shutil.move(path+"/CmdOS-main/"+file,path)
            os.rmdir(path+"/CmdOS-main")
            print("Finalisation...")
            os.remove(path+"/user/readme.txt")
            os.remove(path+"/logs/readme.txt")
            versiontxt=open(path+"/cmdversion.txt","r")
            version=versiontxt.readlines()
            version=version[0]
            versiontxt.close()
            print("CmdOS v"+version+" a bien été installé dans le répertoire "+path)
        else:
            print("Une erreur s'est produite, veuiller vérifier que le répertoire existe et qu'il est vide.")
    elif chose=="d":
        path=input("Veullier indiquer le répertoire où CmdOS est installé : ")
        print("Vérification du répertoire...")
        if os.path.exists(path)==True and "CmdOS.py" in os.listdir(path):
            print("Supression en cours...")
            list_file=os.listdir(path)
            for file in list_file:
                if os.path.isdir(path+"/"+file)==False:
                    print("Supression du fichier "+file+" depuis "+path+"/"+file)
                    os.remove(path+"/"+file)
                else:
                    print("Supression du dossier "+file+" depuis "+path+"/"+file)
                    shutil.rmtree(path+"/"+file)
            print("CmdOS a bien été désinstallé dans le répertoire "+path)
        else:
            print("Une erreur s'est produite, veuiller vérifier que le répertoire existe et que CmdOS y est installé.")
    elif chose=="m":
        path=input("Veullier indiquer le répertoire où CmdOS est installé : ")
        print("Vérification du répertoire...")
        if os.path.exists(path)==True and "CmdOS.py" in os.listdir(path):
            print("Sauvegarde des données...")
            list_file=os.listdir(path+"/user")
            os.makedirs(path+"/save")
            for file in list_file:
                print("Déplacement du dossier "+file+" depuis "+path+"/user/"+file+" vers "+path+"/save")
                shutil.move(path+"/user/"+file,path+"/save")
            versiontxt=open(path+"/cmdversion.txt","r")
            version=versiontxt.readlines()
            version=version[0]
            versiontxt.close()
            print("La version actelle est "+version)
            print("Désinstallation de l'ancienne version...")
            list_file=os.listdir(path)
            for file in list_file:
                if not file=="save":
                    if os.path.isdir(path+"/"+file)==False:
                        print("Supression du fichier "+file+" depuis "+path+"/"+file)
                        os.remove(path+"/"+file)
                    else:
                        print("Supression du dossier "+file+" depuis "+path+"/"+file)
                        shutil.rmtree(path+"/"+file)
                else:
                    next
            versiontxt=req.get("https://cmdos.alwaysdata.net/cmdversion.txt",allow_redirects=True)
            open("cmdversion.txt","wb").write(versiontxt.content)
            vertxt=open("cmdversion.txt","r")
            verlist=vertxt.readlines()
            vertxt.close()
            print("La dernière version est "+verlist[0])
            os.remove("cmdversion.txt")
            print("Installation de la nouvelle version...")
            print("Récupération des fichiers...")
            filename, headers = urllib.request.urlretrieve("https://cmdos.alwaysdata.net/cmdversion.txt", filename=path+"/CmdOS.zip")
            print("Dépaquetage en cours...")
            with zipfile.ZipFile(path+"/CmdOS.zip","r") as zipref:
                zipref.extractall(path)
            os.remove(path+"/CmdOS.zip")
            list_file=os.listdir(path+"/CmdOS-main")
            for file in list_file:
                print("Déplacement du fichier "+file+" depuis "+path+"/CmdOS-main/"+file+" vers "+path)
                shutil.move(path+"/CmdOS-main/"+file,path)
            os.rmdir(path+"/CmdOS-main")
            print("Restauration des données...")
            list_file=os.listdir(path+"/save")
            for file in list_file:
                print("Restauration du compte utilisateur "+file+" depuis "+path+"/save/"+file+" vers "+path+"/user")
                shutil.move(path+"/save/"+file,path+"/user")
            print("Finalisation...")
            os.remove(path+"/user/readme.txt")
            try:
                if "readme.txt" in os.listdir(path+"/logs"):
                    os.remove(path+"/logs/readme.txt")
            except:
                pass
            shutil.rmtree(path+"/save")
            print("CmdOS a bien été mis à jour dans le répertoire "+path+" vers la version "+verlist[0])
        else:
            print("Une erreur s'est produite, veuiller vérifier que le répertoire existe et que CmdOS y est installé.")
elif language=="en":
    chose=input("Do you want to install (i), uninstall (u) ou update CmdOS (up) : ")
    if chose=="i":
        path=input("Please indicate the directory where you want to install CmdOS (it must be empty) : ")
        print("Checking directory...")
        if os.path.exists(path)==True and os.listdir(path)==[]:
            print("Recovering files...")
            filename, headers = urllib.request.urlretrieve("https://github.com/lolo859/CmdOS/archive/refs/heads/main.zip", filename=path+"/CmdOS.zip")
            print("Unpacking in progress...")
            with zipfile.ZipFile(path+"/CmdOS.zip","r") as zipref:
                zipref.extractall(path)
            os.remove(path+"/CmdOS.zip")
            list_file=os.listdir(path+"/CmdOS-main")
            for file in list_file:
                print("Moving file"+file+" from "+path+"/CmdOS-main/"+file+" to "+path)
                shutil.move(path+"/CmdOS-main/"+file,path)
            os.rmdir(path+"/CmdOS-main")
            print("Finishing...")
            os.remove(path+"/user/readme.txt")
            os.remove(path+"/logs/readme.txt")
            versiontxt=open(path+"/cmdversion.txt","r")
            version=versiontxt.readlines()
            version=version[0]
            versiontxt.close()
            print("CmdOS v"+version+" has been intalled in the directory "+path)
        else:
            print("An error has occurred, please verify that the directory exists and is empty.")
    elif chose=="u":
        path=input("Please indicate the directory where CmdOS is installed:")
        print("Checking directory...")
        if os.path.exists(path)==True and "CmdOS.py" in os.listdir(path):
            print("Deleting in progress...")
            list_file=os.listdir(path)
            for file in list_file:
                if os.path.isdir(path+"/"+file)==False:
                    print("Deleting file "+file+" from "+path+"/"+file)
                    os.remove(path+"/"+file)
                else:
                    print("Deleting directory "+file+" from "+path+"/"+file)
                    shutil.rmtree(path+"/"+file)
            print("CmdOS was successfully uninstalled in the directory "+path)
        else:
            print("An error has occurred, please check that the directory exists and that CmdOS is installed there.")
    elif chose=="up":
        path=input("Please indicate the directory where CmdOS is installed : ")
        print("Checking directory...")
        if os.path.exists(path)==True and "CmdOS.py" in os.listdir(path):
            print("Saving data...")
            list_file=os.listdir(path+"/user")
            os.makedirs(path+"/save")
            for file in list_file:
                print("Moving directory "+file+" from "+path+"/user/"+file+" to "+path+"/save")
                shutil.move(path+"/user/"+file,path+"/save")
            versiontxt=open(path+"/cmdversion.txt","r")
            version=versiontxt.readlines()
            version=version[0]
            versiontxt.close()
            print("The current version is "+version)
            print("Uninstalling the old version...")
            list_file=os.listdir(path)
            for file in list_file:
                if not file=="save":
                    if os.path.isdir(path+"/"+file)==False:
                        print("Deleting file "+file+" from "+path+"/"+file)
                        os.remove(path+"/"+file)
                    else:
                        print("Deleting directory "+file+" from "+path+"/"+file)
                        shutil.rmtree(path+"/"+file)
                else:
                    next
            versiontxt=req.get("https://biotech-online.pagesperso-orange.fr/Mathias/cmdversion",allow_redirects=True)
            open("cmdversion.txt","wb").write(versiontxt.content)
            vertxt=open("cmdversion.txt","r")
            verlist=vertxt.readlines()
            vertxt.close()
            print("The latest version is "+verlist[0])
            os.remove("cmdversion.txt")
            print("Installing the latest version...")
            print("Recovering files...")
            filename, headers = urllib.request.urlretrieve("https://github.com/lolo859/CmdOS/archive/refs/heads/main.zip", filename=path+"/CmdOS.zip")
            print("Unpacking in progress...")
            with zipfile.ZipFile(path+"/CmdOS.zip","r") as zipref:
                zipref.extractall(path)
            os.remove(path+"/CmdOS.zip")
            list_file=os.listdir(path+"/CmdOS-main")
            for file in list_file:
                print("Moving file "+file+" from "+path+"/CmdOS-main/"+file+" to "+path)
                shutil.move(path+"/CmdOS-main/"+file,path)
            os.rmdir(path+"/CmdOS-main")
            print("Restoring data...")
            list_file=os.listdir(path+"/save")
            for file in list_file:
                print("Restoring user account "+file+" from "+path+"/save/"+file+" to "+path+"/user")
                shutil.move(path+"/save/"+file,path+"/user")
            print("Finishing...")
            os.remove(path+"/user/readme.txt")
            try:
                if "readme.txt" in os.listdir(path+"/logs"):
                    os.remove(path+"/logs/readme.txt")
            except:
                pass
            shutil.rmtree(path+"/save")
            print("CmdOS has been successfully updated in the directory "+path+" to the version "+verlist[0])
        else:
            print("An error has occurred, please check that the directory exists and that CmdOS is installed there.")
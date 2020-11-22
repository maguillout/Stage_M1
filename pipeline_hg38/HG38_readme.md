Le pipeline hg38 a été adapté (pour chaque commande où il y avait besoin de connaitre la version du génome) mais je n'ai pas pu le tester, à cause des fichiers manquants, il y aura peut-être d'autres adaptations à faire

Le script _download_references_hg38.sh_ contient les commandes pour télécharger les données pour hg38:
- databases annovar
- DBSNP
- MILLS INDELS
- GNOMAD (GRCh38 lifted-over versions of the gnomAD v2 ), attendre 2021 pour la version officielle de l’exome
- fichier de capture: obtenu sur https://sequencing.roche.com/content/dam/rochesequence/worldwide/shared-designs/
- base de données VEP
- genome hg38

    -> il faudrait aussi installer la version hg38 pour CADD avec 
    ```
    pipeline/TOOLS/CADD-scripts/install.sh
    ```

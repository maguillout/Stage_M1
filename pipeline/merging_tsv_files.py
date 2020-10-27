import pandas as pd

inputannovar = snakemake.input[0]
inputintervar = snakemake.input[1]
inputgnomad_vep = snakemake.input[2]
inputcadd = snakemake.input[3]
genes_list=snakemake.params[0].split(',')
#sample=snakemake.params[1]

annovar=pd.read_csv(inputannovar,sep='\t')
cadd=pd.read_csv(inputcadd,sep='\t')
intervar=pd.read_csv(inputintervar,sep='\t')
gnomad_vep=pd.read_csv(inputgnomad_vep,sep='\t')

cadd_reduct=cadd.loc[:,['#Chrom','Pos','Ref','Alt', 'Consequence', 'GeneID', 'FeatureID', 'CCDS', 'CDSpos', 'Exon', 'SIFTcat', 'SIFTval', 'PolyPhenCat', 'PolyPhenVal', 'PHRED']]
cadd_reduct.columns=['CHROM','POS','REF','ALT', 'Consequence','GeneID', 'FeatureID', 'CCDS', 'CDSpos', 'Exon', 'SIFTcat', 'SIFTval', 'PolyPhenCat', 'PolyPhenVal', 'CADD SCORE']
### CADD add a line for each variant which has different ENS_id names, so we have to keep only the lines with the correct ENS_id
cadd_reduct=cadd_reduct[cadd_reduct['GeneID'].isin(genes_list)]
####build of ACMG criteria table, separate by level of criteria
acmg=intervar[' InterVar: InterVar and Evidence ']
acmg_details=acmg.str.split(r"PVS1", n=-1,expand=True)[1]
intervar['Automatic Interpretation']=acmg.str.split(r"PVS1", n=-1,expand=True)[0]
intervar['Automatic Interpretation']=intervar['Automatic Interpretation'].str.replace("InterVar: ","")
arguments = ['PVS1','PS','PM','PP','BA1','BS','BP']
for a in arguments:
    acmg_details=acmg_details.str.replace(a,"")

acmg_details=acmg_details.str.split(r"=", n=-1,expand=True)
del acmg_details[0]
acmg_details.columns=arguments

#get AA change information, the same value is repeated, so we have to get the first one
gnomad_vep['Amino_acids']=gnomad_vep['Amino_acids'].str.split(',', n=-1,expand=True)[0]
gnomad_vep['Codons']=gnomad_vep['Codons'].str.split(',', n=-1,expand=True)[0]
gnomad_vep['CLIN_SIG']=gnomad_vep['CLIN_SIG'].str.split(',', n=-1,expand=True)[0]
gnomad_vep['PUBMED']=gnomad_vep['PUBMED'].str.split(',', n=-1,expand=True)[0]
intervar['Orpha']=intervar['Orpha'].str.split('|', n=-1,expand=True)[1]

intervar_reduct=intervar.loc[:,['#Chr', 'Start', 'Ref','Alt', 'Ref.Gene', 'avsnp147','Automatic Interpretation','clinvar: Clinvar ','Orpha','AAChange.knownGene']]
intervar_reduct.columns=['CHROM','Start','Ref','Alt','Gene name', 'ID','Automatic Interpretation','Clinvar ','Orpha','AAChange.knownGene']
intervar_reduct=pd.concat([intervar_reduct,acmg_details],axis = 1)

annovar_reduct=annovar.loc[:,['Chr', 'Start','Ref','Alt','End','REVEL_score','REVEL_rankscore','Otherinfo5','Otherinfo7','Otherinfo8','gwasCatalog']]
annovar_reduct.columns=['CHROM','Start','Ref','Alt','END','REVEL_score','REVEL_rankscore','POS','REF','ALT','gwasCatalog']

#deletion of useless columns from VEP annotations
del gnomad_vep['ID']
#del gnomad_vep['END']
del gnomad_vep['gnomad.AF_AMR']
del gnomad_vep['gnomad.AF_EAS']
del gnomad_vep['gnomad.AF_FIN']
del gnomad_vep['gnomad.AF_OTH']
del gnomad_vep['gnomad.AF_SAS']
del gnomad_vep['Feature']
del gnomad_vep['HGVSc']
del gnomad_vep['HGVSp']
del gnomad_vep['Protein_position']

annovar_intervar=pd.merge(intervar_reduct,annovar_reduct, how='outer',on=['CHROM','Start','Ref','Alt'])

# annovar and intervar left normalize deletions, so POS, REF and ALT fields are not always the same
# "real" POS, REF and ALT were annoted as 'Otherinfo5' ,'Otherinfo7' and 'Otherinfo8' in annovar dataframe, 
# now, they are annoted as POS, REF and ALT so, we can now delete Start, Ref, and Alt
del annovar_intervar['Start']
del annovar_intervar['Ref']
del annovar_intervar['Alt']

annovar_intervar_cadd=pd.merge(annovar_intervar, cadd_reduct,  how='outer',on=['CHROM','POS','ALT','REF'])
annovar_intervar_cadd_vep=pd.merge(gnomad_vep, annovar_intervar_cadd,  how='outer',on=['CHROM','POS','REF','ALT'])
#to remove variants which are considered as "benign" by Intervar
main_results=annovar_intervar_cadd_vep[annovar_intervar_cadd_vep['Automatic Interpretation'].str.find("Benign") != 1]

main_results.to_csv(f'CSV/individual_results.tsv',sep='\t',index=False)

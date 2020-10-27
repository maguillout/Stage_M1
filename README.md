Exome analysis
==============
This application comprises an analysis pipeline and a graphical interface

The main steps of the pipeline are:
- alignment of reads on reference genome with [bwa](http://bio-bwa.sourceforge.net/)
- marking of duplicates with [picard](http://broadinstitute.github.io/picard/)
- realignment around indels with [GATK IndelRealigner](https://software.broadinstitute.org/gatk/)
- base recalibration with [GATK BaseRecalibrator](https://software.broadinstitute.org/gatk/documentation/article.php?id=44)
- variant calling with [GATK HaplotypeCaller](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_haplotypecaller_HaplotypeCaller.php)
- annotation with [gnomAD](http://gnomad.broadinstitute.org/) population frequencies
- annotation with [Variant Effect Predictor](http://www.ensembl.org/info/docs/tools/vep/index.html)  
- annotation with [ANNOVAR](https://doc-openbio.readthedocs.io/projects/annovar/en/latest/)  
- interpretation of variants with [InterVar](https://github.com/WGLab/InterVar)  

The graphical interface can lead to:
- initialise the analysis pipeline
- analyze the variants
- etablish and manage a database

## Tools
### Pipeline
- [Snakemake](https://snakemake.readthedocs.io/)

### Graphical Interface:
-  [Django](https://www.djangoproject.com/)


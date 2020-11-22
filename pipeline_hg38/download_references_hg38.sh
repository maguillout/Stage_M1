## DOWNLOAD DBSNP
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/dbsnp_138.hg38.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/dbsnp_138.hg38.vcf.gz"
tabix -f -p vcf "REFERENCES/dbsnp_138.hg38.vcf.gz"
echo "DBSNP downloaded"

### DOWNLOAD MILLS INDELS
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/Mills_and_1000G_gold_standard.hg38.vcf.gz"
tabix -f -p vcf "REFERENCES/Mills_and_1000G_gold_standard.hg38.vcf.gz"
echo "MILLS INDELS downloaded"

### DOWNLOAD 1K INDELS 
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/1000G_phase1.snps.high_confidence.hg38.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/1000G_phase1.indels.hg38.vcf.gz"
tabix -f -p vcf "REFERENCES/1000G_phase1.indels.hg38.vcf.gz"
echo "1K INDELS downloaded"

### DOWNLOAD GNOMAD
wget -q --retry-connrefused "https://storage.googleapis.com/gnomad-public/release/2.0.1/vcf/exomes/gnomad.exomes.r2.0.1.sites.vcf.gz" -O "REFERENCES/gnomad.exomes.r2.0.1.sites.vcf.gz"
tabix -f -p vcf "REFERENCES/gnomad.exomes.r2.0.1.sites.vcf.gz"
echo "GNOMAD downloaded"

### DOWNLOAD CAPTURE
wget "https://sequencing.roche.com/content/dam/rochesequence/worldwide/shared-designs/MedExome_design_files.zip" -O "REFERENCES/MedExome_hg38_empirical_targets.interval_list.gz"
gunzip -c  "REFERENCES/MedExome_hg38_empirical_targets.interval_list.gz" | grep -v "^@" | cut -f1-3 | awk '{{print $1"\t"$2-1"\t"$3}}' > "REFERENCES/MedExome_hg38_empirical_targets.bed"
echo "CAPTURE downloaded"

### DOWNLOAD GENOME
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/Homo_sapiens_assembly38.fasta.gz" -O "REFERENCES/Homo_sapiens_assembly38.fasta.gz",
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/Homo_sapiens_assembly38.fasta.fai" -O "REFERENCES/Homo_sapiens_assembly38.fasta.fai"
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/hg38/Homo_sapiens_assembly38.dict" -O "REFERENCES/Homo_sapiens_assembly38.dict"
echo "GENOME downloaded"


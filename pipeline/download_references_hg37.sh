## DOWNLOAD DBSNP
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/b37/dbsnp_138.b37.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/b37/dbsnp_138.b37.vcf.gz",
tabix -f -p vcf "REFERENCES/b37/dbsnp_138.b37.vcf.gz"
echo "DBSNP downloaded"

### DOWNLOAD MILLS INDELS
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/b37/Mills_and_1000G_gold_standard.indels.b37.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/Mills_and_1000G_gold_standard.b37.vcf.gz"
tabix -f -p vcf "REFERENCES/Mills_and_1000G_gold_standard.b37.vcf.gz"
echo "MILLS INDELS downloaded"


### DOWNLOAD 1K INDELS 
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/b37/1000G_phase1.indels.b37.vcf.gz" -O - | gunzip -c | bgzip > "REFERENCES/1000G_phase1.indels.b37.vcf.gz"
tabix -f -p vcf "REFERENCES/1000G_phase1.indels.b37.vcf.gz"
echo "1K INDELS downloaded"

### DOWNLOAD GNOMAD
wget -q --retry-connrefused "https://storage.googleapis.com/gnomad-public/release/2.0.1/vcf/exomes/gnomad.exomes.r2.0.1.sites.vcf.gz" -O "REFERENCES/gnomad.exomes.r2.0.1.sites.vcf.gz"
tabix -f -p vcf "REFERENCES/gnomad.exomes.r2.0.1.sites.vcf.gz"
echo "GNOMAD downloaded"

### DOWNLOAD CAPTURE
wget "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/b37/Broad.human.exome.b37.interval_list.gz" -O "REFERENCES/Broad.human.exome.b37.interval_list.gz"
gunzip -c  "REFERENCES/Broad.human.exome.b37.interval_list.gz" | grep -v "^@" | cut -f1-3 | awk '{{print $1"\t"$2-1"\t"$3}}' > "REFERENCES/Broad.human.exome.b37.bed"
echo "CAPTURE downloaded"

### DOWNLOAD GENOME
wget -q --retry-connrefused --user=gsapubftp-anonymous "ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/b37/human_g1k_v37.fasta.gz" -O "REFERENCES/human_g1k_v37.fasta.gz"
echo "GENOME downloaded"


Title: Small RNA deep sequencing for transgenic Sr2 candidate gene

This project is to understand how the RNAi construct affects the expression of small RNAs in wheat with or without infection with stem rust.

Background

Stem rust is a serious disease and decreases wheat yield. Stem rust resistance gene Sr2 provides race non- specific adult plant resistance against all races of 
stem rust and is also linked to leaf rust, stripe rust and powdery mildew resistance. The data was produced from sRNA sequencing of rust infected lines silenced 
for the candidate gene and the wildtype parent.  
Initial sRNA gels indicated that the wild type parent may be undergoing some silencing and hence the need to do the sRNA deep sequencing. Also, there is evidence
of Sr2 being effected by other genes and sRNA sequencing could help us find other interacting partners. 
  
Data collection

RNAi construct for one of Sr2 candidate gene was generated and transformed into wheat (Chinese Spring). Two wild tpye plants and two transgenic plants were infected \
with stem rust and leaf materials were harvested at o hr and 48 hrs after rust treatment. The samples label as the following:
1. wild type (WT1), 0 hr
2. wild type (WT1), 48 hrs 
3. wild type (WT2), 0 hr
4. wild type (WT2), 48 hrs
5. PC174_1_56 (T1), 0 hr
6. PC174_1_56 (T1), 48 hr
7. PC174_8_58 (T2), 0 hr
8. PC174_8_58 (T2), 48 hr


Total RNA was isolated by Trizol and quality was checked either by agarose gel or Quebit quantification. The RNA samples were sent to AGRF centre for small deep seqencing.
The raw data as the following:
1_CCRENANXX_ATCACG_L008_R1.fastq.gz
2_CCRENANXX_CGATGT_L008_R1.fastq.gz
3_CCRENANXX_TTAGGC_L008_R1.fastq.gz
4_CCRENANXX_TGACCA_L008_R1.fastq.gz
5_CCRENANXX_ACAGTG_L008_R1.fastq.gz
6_CCRENANXX_GCCAAT_L008_R1.fastq.gz
7_CCRENANXX_CAGATC_L008_R1.fastq.gz
8_CCRENANXX_ACTTGA_L008_R1.fastq.gz 

Based on the previous report (Ragupathy et al., 2016, Deep sequencing of wheat sRNA transcriptome reveals distinct temporal expression pattern of miRNAs in response to heat, light 
and UV, Scientific reports), the selection criteria for process small RNA are:
--trim the adapter
--filter the sRNA between 18 to 24 Nts
--filter the sRNA with the reads >= 10 RPM 

# Description

This project implementes a reproducible, containerized pipeline that takes raw FASTQ reads through:
* FastQC
* Trimmomatic
* HISAT2 (alignment)
* SAMtools (sort/index)
* MultiQC (report)

![Snakemake](https://img.shields.io/badge/workflow-Snakemake-brightgreen)
![Bioconda](https://img.shields.io/badge/install-bioconda-blue)
![CI](https://github.com/Ramanuj-Sarkar/genomics-pipeline-starter/actions/workflows/test_pipeline.yml/badge.svg)

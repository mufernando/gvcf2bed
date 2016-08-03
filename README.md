GVCF2BED
========

This is a small tool to convert a gVCF file to BED.
This is useful for extracting regions that pass a certain genotype quality threshold. 


## Requirements

* Python 3.4+
* pyvcf

### For developers

* pytest
* pytest-cov


## Usage

```
usage: gvcf2bed.py [-h] -I INPUT -O OUTPUT [-s SAMPLE] [-q QUALITY]

Create a BED file from a gVCF. Regions are based on a minimum genotype
quality. The gVCF file must contain a GQ field in its FORMAT fields.

optional arguments:
  -h, --help            show this help message and exit
  -I INPUT, --input INPUT
                        Input gVCF
  -O OUTPUT, --output OUTPUT
                        Output bed file
  -s SAMPLE, --sample SAMPLE
                        Sample name in VCF file to use. Will default to first
                        sample (alphabetically) if not supplied
  -q QUALITY, --quality QUALITY
                        Minimum genotype quality (default 20)
```
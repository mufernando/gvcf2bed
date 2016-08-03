"""
gvcf2bed tests
~~~~~~~~~~~~~~~~

:copyright: (c) 2016 Sander Bollen
:license: MIT
"""
import vcf
import pytest
from gvcf2bed import *


@pytest.fixture()
def mini_reader():
    reader = vcf.Reader(filename="test/data/mini.vcf")
    return reader


@pytest.fixture()
def block_reader():
    reader = vcf.Reader(filename="test/data/block.vcf")
    return reader


class TestFunctions(object):

    def test_gqx_mini(self, mini_reader):
        gqx = [get_gqx(x, "Sample_01") for x in mini_reader]
        assert len(gqx) == 11
        assert gqx == [20.0, 21.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0]

    def test_gqx_block(self, block_reader):
        gqx = [get_gqx(x, "Sample_01") for x in block_reader]
        assert len(gqx) == 10
        assert gqx == [3.0, 5.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]

    def test_bedline(self):
        tmp = BedLine("chr1", 500, 600)
        assert str(tmp) == "chr1\t500\t600"

    def test_vcf2bed(self, mini_reader):
        records = [vcf_record_to_bed(x) for x in mini_reader]
        assert len(records) == 11
        assert str(records[0]) == "chr1\t156084708\t156084709"

    def test_vcf2bed_block(self, block_reader):
        records = [vcf_record_to_bed(x) for x in block_reader]
        assert len(records) == 10
        assert str(records[0]) == "chr1\t83880332\t83880428"





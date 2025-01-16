import pytest
from main import main
# Benchmark the RSA encryption and decryption process using pytest-benchmark
@pytest.mark.benchmark(group="rsa")
def test_rsa_benchmark(benchmark):
    result = benchmark(main)
    assert result == "Werde Mitglied bei Wikipedia!"
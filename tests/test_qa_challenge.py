import subprocess

def test_qa():
    result = subprocess.run(["behave", "features/qa.feature"], capture_output=True, text=True)
    print(result.stdout)
    assert result.returncode == 0, f"Behave tests failed:\n{result.stdout}"

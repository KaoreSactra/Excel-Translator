import subprocess

scripts = [
    "scripts/desblock.py",
    "scripts/translator.py"
]

for script in scripts:
    print(f"Executando {script}...")
    subprocess.run(["python", script])
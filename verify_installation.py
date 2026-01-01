# verify_installation.py
import sys
import importlib

packages = [
    "numpy", "pandas", "sklearn", "skfuzzy", 
    "cv2", "matplotlib", "seaborn", 
    "nltk", "torch", "tensorflow"
]

print("=== Cek Library & Versi ===")
for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        print(f"{pkg}: OK, version = {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"{pkg}: ERROR → {e}")

print("\nPython:", sys.version)

# Tambahan: cek iris dataset
print("\n=== Iris Dataset Check ===")
try:
    from sklearn import datasets
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    print("Iris shape:", X.shape)
    print("Feature names:", iris.feature_names)
except Exception as e:
    print("Iris dataset load ERROR →", e)

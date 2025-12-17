import nbformat
from nbformat.sign import NotebookNotary

filename = "Analyse_Covid.ipynb"

try:
    notary = NotebookNotary()
    nb = nbformat.read(filename, as_version=4)
    notary.sign(nb)
    nbformat.write(nb, filename)
    print(f"Succès ! Le notebook '{filename}' est maintenant de confiance (Trusted).")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{filename}' est introuvable. Vérifiez que vous êtes dans le bon dossier.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
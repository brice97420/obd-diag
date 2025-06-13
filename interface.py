
import tkinter as tk
from tkinter import messagebox, filedialog
from kline_utils import lire_dtc, reveiller_ecu, reset_comm, lire_bin, ecrire_bin, passer_en_boot

def lancer_interface():
    fenetre = tk.Tk()
    fenetre.title("Diag MPPS V18 - SID801")
    fenetre.geometry("400x400")

    label = tk.Label(fenetre, text="Interface de Diagnostic MPPS V18", font=("Arial", 14))
    label.pack(pady=10)

    bouton_dtc = tk.Button(fenetre, text="Lire les DTC", command=lire_dtc)
    bouton_dtc.pack(pady=5)

    bouton_reveil = tk.Button(fenetre, text="Réveiller l'ECU", command=reveiller_ecu)
    bouton_reveil.pack(pady=5)

    bouton_reset = tk.Button(fenetre, text="Réinitialiser Communication", command=reset_comm)
    bouton_reset.pack(pady=5)

    bouton_lire = tk.Button(fenetre, text="Lire fichier .bin", command=lambda: lire_bin(filedialog.asksaveasfilename(defaultextension=".bin")))
    bouton_lire.pack(pady=5)

    bouton_ecrire = tk.Button(fenetre, text="Écrire fichier .bin", command=lambda: ecrire_bin(filedialog.askopenfilename(filetypes=[("Fichiers BIN", "*.bin")])))
    bouton_ecrire.pack(pady=5)

    bouton_boot = tk.Button(fenetre, text="Mode Boot (Pin 28)", command=passer_en_boot)
    bouton_boot.pack(pady=5)

    bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
    bouton_quitter.pack(pady=20)

    fenetre.mainloop()

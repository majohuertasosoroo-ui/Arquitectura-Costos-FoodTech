import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from Backend.gastronomia import ControlCostos

class AppFoodTech:
    def __init__(self, root):
        self.root = root
        self.root.title("Food-Tech - Monitor de Inflación")
        self.root.geometry("400x550")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)
        self.construir_gui()

    def construir_gui(self):
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(base_dir, "logo.png")
            img = Image.open(logo_path).convert("RGB").resize((120, 120), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo_img, bg="#f4f4f4").pack(pady=10)
        except Exception:
            tk.Label(self.root, text="🍳 CHEF-COSTOS", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=20)

        tk.Label(self.root, text="Monitor de Insumos", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=5)

        tk.Label(self.root, text="Nombre del Ingrediente:", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.entry_ingrediente = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_ingrediente.pack(pady=5)

        tk.Label(self.root, text="Precio Mes Anterior ($):", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.entry_anterior = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_anterior.pack(pady=5)

        tk.Label(self.root, text="Precio Mercado Actual ($):", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.entry_actual = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_actual.pack(pady=5)

        tk.Button(self.root, text="📊 Auditar Precio", bg="#e63946", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=self.registrar).pack(pady=15, fill="x", padx=50)
        tk.Button(self.root, text="🧹 Limpiar", bg="#457b9d", fg="white", cursor="hand2", command=self.limpiar).pack(pady=5, fill="x", padx=120)

    def registrar(self):
        ingrediente = self.entry_ingrediente.get().strip()
        ant_str = self.entry_anterior.get().strip()
        act_str = self.entry_actual.get().strip()

        try:
            if not ingrediente or not ant_str or not act_str:
                raise ValueError("Debe ingresar el ingrediente y ambos precios.")
            
            try:
                p_anterior = float(ant_str)
                p_actual = float(act_str)
            except ValueError:
                raise ValueError("Los precios deben ser valores numéricos.")

            if p_anterior <= 0 or p_actual <= 0:
                raise ValueError("Los precios deben ser mayores a 0.")

            # Lógica de Negocio: Cálculo de Inflación y Alertas
            inflacion = ((p_actual - p_anterior) / p_anterior) * 100
            alerta = "ALERTA" if inflacion >= 20.0 else "ESTABLE"

            ControlCostos.guardar_costo(ingrediente, p_anterior, p_actual, inflacion, alerta)
            
            # Alerta visual
            if alerta == "ALERTA":
                messagebox.showwarning("⚠️ Alerta de Inflación", f"{ingrediente} ha subido un {inflacion:.1f}%.\nEstado: {alerta}")
            else:
                messagebox.showinfo("✅ Precio Estable", f"{ingrediente} varió un {inflacion:.1f}%.\nEstado: {alerta}")
            
            self.limpiar()

        except ValueError as ve:
            messagebox.showwarning("Advertencia", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Fallo en el sistema:\n{e}")

    def limpiar(self):
        self.entry_ingrediente.delete(0, tk.END)
        self.entry_anterior.delete(0, tk.END)
        self.entry_actual.delete(0, tk.END)
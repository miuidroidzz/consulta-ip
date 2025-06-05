#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

# Cores e estilo simples
TITLE = "Consulta Simples - By Miuidroidzz"

def consulta_ip():
    ip = simpledialog.askstring("Consulta IP", "Digite o IP para consultar:")
    if ip:
        url = f"http://ip-api.com/json/{ip}"
        try:
            res = requests.get(url).json()
            if res.get("status") == "success":
                info = f"""
IP: {res.get("query")}
País: {res.get("country")}
Região: {res.get("regionName")}
Cidade: {res.get("city")}
ISP: {res.get("isp")}
Latitude: {res.get("lat")}
Longitude: {res.get("lon")}
"""
                messagebox.showinfo("Resultado Consulta IP", info)
            else:
                messagebox.showerror("Erro", "IP inválido ou não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na consulta: {e}")

def consulta_cep():
    cep = simpledialog.askstring("Consulta CEP", "Digite o CEP para consultar (apenas números):")
    if cep and len(cep) == 8 and cep.isdigit():
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            res = requests.get(url).json()
            if "erro" not in res:
                info = f"""
CEP: {res.get('cep')}
Logradouro: {res.get('logradouro')}
Bairro: {res.get('bairro')}
Cidade: {res.get('localidade')}
Estado: {res.get('uf')}
"""
                messagebox.showinfo("Resultado Consulta CEP", info)
            else:
                messagebox.showerror("Erro", "CEP não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na consulta: {e}")
    else:
        messagebox.showerror("Erro", "CEP inválido. Deve ter 8 dígitos numéricos.")

def consulta_cnpj():
    cnpj = simpledialog.askstring("Consulta CNPJ", "Digite o CNPJ para consultar (apenas números):")
    if cnpj:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        try:
            res = requests.get(url).json()
            if res.get("status") != "ERROR":
                info = f"""
Nome: {res.get('nome')}
Fantasia: {res.get('fantasia')}
Atividade Principal: {res.get('atividade_principal')[0]['text']}
Situação: {res.get('situacao')}
Telefone: {res.get('telefone')}
Email: {res.get('email')}
"""
                messagebox.showinfo("Resultado Consulta CNPJ", info)
            else:
                messagebox.showerror("Erro", "CNPJ inválido ou não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na consulta: {e}")
    else:
        messagebox.showerror("Erro", "CNPJ inválido.")

def sair():
    root.destroy()

# Janela principal
root = tk.Tk()
root.title(TITLE)
root.geometry("350x250")

label = tk.Label(root, text="Consultas Disponíveis", font=("Arial", 14))
label.pack(pady=10)

btn_ip = tk.Button(root, text="Consulta IP", width=25, command=consulta_ip)
btn_ip.pack(pady=5)

btn_cep = tk.Button(root, text="Consulta CEP", width=25, command=consulta_cep)
btn_cep.pack(pady=5)

btn_cnpj = tk.Button(root, text="Consulta CNPJ", width=25, command=consulta_cnpj)
btn_cnpj.pack(pady=5)

btn_exit = tk.Button(root, text="Sair", width=25, command=sair)
btn_exit.pack(pady=20)

root.mainloop()
# Fim do código
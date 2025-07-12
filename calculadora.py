import tkinter as tk
from tkinter import font

class ModernCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Moderna")
        master.geometry("320x500")
        master.resizable(False, False)
        master.configure(bg='#121212')
        
        # Configuração de estilo
        self.bg_color = '#121212'
        self.display_bg = '#1e1e1e'
        self.button_bg = '#2d2d2d'
        self.operation_bg = '#ff9500'
        self.special_bg = '#a5a5a5'
        self.text_color = '#ffffff'
        self.hover_color = '#3d3d3d'
        self.active_color = '#4d4d4d'
        
        # Fonte moderna
        self.display_font = font.Font(family='Segoe UI', size=32, weight='normal')
        self.button_font = font.Font(family='Segoe UI', size=16, weight='normal')
        
        # Variáveis
        self.current_input = ""
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        self.display = tk.Label(
            self.master, 
            text="0", 
            anchor='e', 
            bg=self.display_bg, 
            fg=self.text_color, 
            font=self.display_font,
            padx=20,
            pady=20
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        # Botões
        buttons = [
            ('C', 1, 0, self.special_bg), ('±', 1, 1, self.special_bg), ('%', 1, 2, self.special_bg), ('÷', 1, 3, self.operation_bg),
            ('7', 2, 0, self.button_bg), ('8', 2, 1, self.button_bg), ('9', 2, 2, self.button_bg), ('×', 2, 3, self.operation_bg),
            ('4', 3, 0, self.button_bg), ('5', 3, 1, self.button_bg), ('6', 3, 2, self.button_bg), ('-', 3, 3, self.operation_bg),
            ('1', 4, 0, self.button_bg), ('2', 4, 1, self.button_bg), ('3', 4, 2, self.button_bg), ('+', 4, 3, self.operation_bg),
            ('0', 5, 0, self.button_bg), ('.', 5, 2, self.button_bg), ('=', 5, 3, self.operation_bg)
        ]
        
        # Configuração de grid
        self.master.grid_rowconfigure(0, weight=1)
        for i in range(1, 6):
            self.master.grid_rowconfigure(i, weight=1, minsize=70)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        
        # Criar botões
        for (text, row, col, bg) in buttons:
            # Botão 0 especial (mais largo)
            if text == '0':
                btn = tk.Button(
                    self.master, 
                    text=text, 
                    font=self.button_font,
                    bg=bg,
                    fg=self.text_color,
                    activebackground=self.active_color,
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=1, pady=1)
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.hover_color))
                btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))
            else:
                btn = tk.Button(
                    self.master, 
                    text=text, 
                    font=self.button_font,
                    bg=bg,
                    fg=self.text_color,
                    activebackground=self.active_color,
                    borderwidth=0,
                    highlightthickness=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.hover_color))
                btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))
    
    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""
            self.display.config(text="0")
        elif char == '±':
            if self.current_input and self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        elif char == '%':
            try:
                self.current_input = str(eval(self.current_input + "/100"))
            except:
                self.current_input = ""
                self.display.config(text="Erro")
        elif char == '=':
            try:
                expr = self.current_input.replace('×', '*').replace('÷', '/')
                result = str(eval(expr))
                self.current_input = result
                self.display.config(text=result)
            except:
                self.current_input = ""
                self.display.config(text="Erro")
        else:
            self.current_input += char
            self.display.config(text=self.current_input)

# Criar e rodar a aplicação
root = tk.Tk()
app = ModernCalculator(root)
root.mainloop()
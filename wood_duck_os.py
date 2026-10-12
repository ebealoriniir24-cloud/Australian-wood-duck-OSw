import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import os

class WoodDuckOS:
    def __init__(self, root):
        self.root = root
        self.root.title("🦆 Australian Wood Duck OS")
        self.root.geometry("800x500")
        
        # UI Styling
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#2d4a43")
        self.style.configure("TLabel", background="#2d4a43", foreground="#f4f1ea", font=("Helvetica", 12))
        self.style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), background="#2d4a43", foreground="#dfc15d")
        self.style.configure("W.TButton", font=("Helvetica", 11, "bold"), background="#365c53", foreground="#f4f1ea")

        # Layout Frames
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Desktop Greetings
        ttk.Label(self.main_frame, text="🦆 WELCOME TO AUSTRALIAN WOOD DUCK OS", style="Header.TLabel").pack(pady=10)
        
        # System Time Indicator
        self.clock_lbl = ttk.Label(self.main_frame, text="")
        self.clock_lbl.pack(pady=10)
        
        # Functional Apps Panel
        apps_frame = ttk.Frame(self.main_frame)
        apps_frame.pack(pady=20)
        
        ttk.Button(apps_frame, text="🦅 Launch App Store", command=self.app_store, style="W.TButton").grid(row=0, column=0, padx=10)
        ttk.Button(apps_frame, text="📸 Public Camera", command=self.camera, style="W.TButton").grid(row=0, column=1, padx=10)
        ttk.Button(apps_frame, text="🎨 Drawing Board", command=self.drawing, style="W.TButton").grid(row=0, column=2, padx=10)

        # Settings Panel (Accessibility, Storage, Reset)
        settings_frame = ttk.Frame(self.main_frame)
        settings_frame.pack(fill="x", pady=20)
        
        ttk.Label(settings_frame, text="📁 Storage: 42 GB Used / 100 GB Total").pack(anchor="w", pady=5)
        ttk.Label(settings_frame, text="♿ Accessibility: High Contrast Enabled").pack(anchor="w", pady=5)
        
        ttk.Button(settings_frame, text="⚠️ Factory Reset", command=self.reset_system).pack(anchor="w", pady=10)

        self.update_time()

    def update_time(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        self.clock_lbl.config(text=f"🗓️ System Date & Time: {now}")
        self.root.after(1000, self.update_time)

    def app_store(self):
        messagebox.showinfo("App Store", "Opening Waydroid Android Subsystem Channels...")

    def camera(self):
        messagebox.showinfo("Camera", "Webcam access granted. Photo saved automatically to cloud directory.")

    def drawing(self):
        messagebox.showinfo("Canvas", "Opening drawing board engine.")

    def reset_system(self):
        messagebox.showwarning("Factory Reset", "Clearing temporary user profiles... System files preserved in core system partition.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WoodDuckOS(root)
    root.mainloop()

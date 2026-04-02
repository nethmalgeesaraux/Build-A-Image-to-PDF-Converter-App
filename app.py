import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image

class ImageToPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter output PDF name:")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

    def select_images(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"),
                ("All files", "*.*"),
            ],
        )

        if file_paths:
            self.image_paths = list(file_paths)
            self.update_image_listbox()

    def update_image_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.selected_images_listbox.insert(tk.END, os.path.basename(path))

    def convert_images_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("Warning", "Please select at least one image.")
            return

        output_name = self.output_pdf_name.get().strip()
        if not output_name:
            messagebox.showwarning("Warning", "Please enter a name for the output PDF.")
            return

        if not output_name.lower().endswith(".pdf"):
            output_name += ".pdf"

        output_path = filedialog.asksaveasfilename(
            initialfile=output_name,
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )

        if not output_path:
            return

        try:
            images = [Image.open(path).convert("RGB") for path in self.image_paths]

            if len(images) == 1:
                images[0].save(output_path)
            else:
                images[0].save(
                    output_path,
                    save_all=True,
                    append_images=images[1:],
                    resolution=100.0,
                )

            messagebox.showinfo(
                "Success",
                f"Successfully converted {len(self.image_paths)} images to PDF!\n\nSaved as: {output_path}",
            )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")
    app = ImageToPDFConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

            
            
    






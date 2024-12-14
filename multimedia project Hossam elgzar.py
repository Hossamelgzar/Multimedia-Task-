import tkinter as tk
from tkinter import ttk

# إنشاء نافذة
root = tk.Tk()
root.title("Text to Speech Form")
root.geometry("400x300")  # حجم النافذة

# العنوان الأساسي
label_title = tk.Label(root, text="Text to Speech", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# إدخال النص
label_input = tk.Label(root, text="Enter Text:")
label_input.pack(anchor="w", padx=10)
entry_input = tk.Entry(root, width=40)
entry_input.pack(padx=10, pady=5)

# الأزرار
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

btn_play = ttk.Button(frame_buttons, text="Play")
btn_play.grid(row=0, column=0, padx=10)

btn_stop = ttk.Button(frame_buttons, text="Stop")
btn_stop.grid(row=0, column=1, padx=10)

btn_set = ttk.Button(frame_buttons, text="Set")
btn_set.grid(row=0, column=2, padx=10)

# إشعارات صغيرة
label_note1 = tk.Label(frame_buttons, text="تشغيل", font=("Arial", 10))
label_note1.grid(row=1, column=0)

label_note2 = tk.Label(frame_buttons, text="إيقاف", font=("Arial", 10))
label_note2.grid(row=1, column=1)

label_note3 = tk.Label(frame_buttons, text="إعداد", font=("Arial", 10))
label_note3.grid(row=1, column=2)

# تشغيل النافذة
root.mainloop()
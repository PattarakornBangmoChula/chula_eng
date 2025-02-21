import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "gor kai"), ("ข", "kho khai"), ("ค", "kho khwai"), ("ง", "ngo ngu"),
    ("จ", "jor jaan"), ("ฉ", "cho ching"), ("ช", "cho chang"), ("ซ", "so so"),
    ("ญ", "yo ying"), ("ด", "dor dek"), ("ต", "tor tao"), ("ถ", "tho thung"),
    ("ป", "por pla"), ("พ", "pho phan"), ("ฟ", "fo fan"), ("ม", "mor maa"),
    ("ร", "ror rua"), ("ล", "lor ling"), ("ว", "wor waen"), ("ส", "so sua")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief=tk.RAISED, borderwidth=3)
        self.card_frame.pack(expand=True)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 48), bg="white")
        self.label.pack(expand=True)
        
        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)
        
        self.current_card = None
        self.showing_name = False
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.showing_name = False
    
    def flip_card(self, event):
        if self.showing_name:
            self.label.config(text=self.current_card[0])
        else:
            self.label.config(text=self.current_card[1])
        self.showing_name = not self.showing_name

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()

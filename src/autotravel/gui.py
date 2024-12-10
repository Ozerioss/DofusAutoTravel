import threading
from tkinter import Tk, Text, Button, Scrollbar, END, Frame, VERTICAL
from clipboard_monitor import ClipboardMonitor


class GUI:
    def __init__(self):
        self.root = Tk()

        self.frame = Frame(self.root)
        self.gui_log = Text(self.frame, wrap="word", state="normal", height=20)

        self.monitor = None
        self.monitor_thread = None

        self.stop_button = Button(
            self.root, text="Stop Monitoring", command=self.stop_monitoring, state="disabled"
        )
        self.start_button = Button(self.root, text="Start Monitoring", command=self.start_monitoring)

        self.setup_gui()

    def setup_gui(self):
        self.root.title("Dofus Travel Helper")
        self.frame.pack(fill="both", expand=True)
        self.gui_log.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(self.frame, command=self.gui_log.yview, orient=VERTICAL)
        scrollbar.pack(side="right", fill="y")

        self.gui_log.config(yscrollcommand=scrollbar.set)

        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button.pack(side="right", padx=10, pady=10)

    def log_message(self, message):
        """Log messages to the GUI."""
        self.gui_log.insert(END, f"{message}\n")
        self.gui_log.see(END)

    def start_monitoring(self):
        """Start clipboard monitoring."""
        if not self.monitor_thread or not self.monitor_thread.is_alive():
            self.monitor = ClipboardMonitor("- Release", gui_log=self.log_message)
            self.monitor_thread = threading.Thread(target=self.monitor.monitor, daemon=True)
            self.monitor_thread.start()
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

    def stop_monitoring(self):
        """Stop clipboard monitoring."""
        if self.monitor:
            self.monitor.stop()
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

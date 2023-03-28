from PyQt5.QtCore import QProcess

def process_finished():
    print("Process finished.")
    p = None


for i in range(10):

    p = None  # Default empty value.
    print("Executing process")
    p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
    p.finished.connect(process_finished)  # Clean up once complete.
    p.start("python", ['test.py'])
    p.terminate()
    p.waitForFinished()
    
    




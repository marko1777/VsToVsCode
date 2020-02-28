import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


DIRECTORY_TO_WATCH = "c:\\code\\m_sw_main\\"
TARGETDIR = "e:\\exp\\sep\\m_sw_main\\"

class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    
    @staticmethod
    def on_any_event(event):
        s = event.src_path.split('\\')
        r = TARGETDIR + ('\\'.join(s[3:]))
        
        if event.event_type == 'created':
            if event.is_directory:
                os.system("md " + r)
            else:
                ss = "mklink " + r + " " + event.src_path
                os.system(ss)
        elif event.event_type == 'deleted':
            if event.is_directory:
                os.system("rmdir " + r)
            else:
                os.system("del " + r)

if __name__ == '__main__':
    w = Watcher()
    w.run()
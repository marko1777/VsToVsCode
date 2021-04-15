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
    
    def Handler(self):
        self.should_create_dir = False
    
    def on_any_event(self, event):
        s = event.src_path.split('\\')
        r = TARGETDIR + ('\\'.join(s[3:]))

        if event.event_type == 'created':
            if event.is_directory:
                self.should_create_dir = True
                # os.system("md " + r)
            else:
                if event.src_path.endswith(".cpp") or event.src_path.endswith(".h"):
                    if self.should_create_dir:
                        rr = TARGETDIR + ('\\'.join(s[3:-1]))
                        os.system("md " + rr)
                        self.should_create_dir = False
                        
                    ss = "mklink " + r + " " + event.src_path
                    print(ss)
                    os.system(ss)
                else:
                    self.should_create_dir = False
                    

        elif event.event_type == 'deleted':
            if event.is_directory:
                print(r)
                os.system("rmdir " + r)
            else:
                if event.src_path.endswith(".cpp") or event.src_path.endswith(".h"):
                    rr = TARGETDIR + ('\\'.join(s[3:-1]))
                    os.system("del " + r)

if __name__ == '__main__':
    w = Watcher()
    w.run()
class Vscode:
    
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    
    def execute(self):
        print("Spell Check")
        print("Convectional Check")
        print("Compiling")
        print("Running")
                

class Laptop:
    
    def code(self, ide):
        ide.execute()

ide = Vscode()

lap1 = Laptop()
lap1.code(ide)   

ide1 = MyEditor()
lap2 = Laptop()
lap2.code(ide1)    
                

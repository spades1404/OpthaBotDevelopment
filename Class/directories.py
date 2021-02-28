import os

class Directories():
    def __init__(self):
        self.cwd = os.getcwd()
        print(self.cwd)
        self.temp = self.cwd + r"\Temp/"
        self.assets = self.cwd + r"\Assets"

        self.currMod = self.cwd + r"\Class\ServerSide\currentModel.txt"
        self.darkTheme = self.assets + r"\dark.qss"
        self.OpthaBotLogo = self.assets + r"\opthabotlogo.png"
        self.icon = self.assets + r"\icon.png"
        self.emptyImageIcon = self.assets + r"\no-image-icon-6.png"
        self.appConfigFile = self.assets + r"\configuration.json"
        self.appPermaSets = self.assets + r"\permaSet.json"
        self.configFile = self.assets + r"\config.json"
        self.keyFile = self.assets + r"\key.json"
        self.model = self.assets +"\Model\model.h5"




if __name__ == "__main__":
    print("hi")
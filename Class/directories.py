import os

class Directories():
    def __init__(self):
        self.cwd = os.getcwd()
        print(self.cwd)
        self.configFile = self.cwd + r"\Database\config.json"
        self.keyFile = self.cwd + r"\Database\key.json"
        self.temp = self.cwd + r"\Temp"
        self.assets = self.cwd + r"\Assets"
        self.model = self.cwd + r"\Tensorflow\Model\model.h5"

        self.currMod = self.cwd + r"\Class\ServerSide\currentModel.txt"
        self.darkTheme = self.assets + r"\dark.qss"
        self.OpthaBotLogo = self.assets + r"\opthabotlogo.png"
        self.icon = self.assets + r"\icon.png"
        self.emptyImageIcon = self.assets + r"\no-image-icon-6.png"
        self.appConfigFile = self.assets + r"\configuration.json"





if __name__ == "__main__":
    print("hi")
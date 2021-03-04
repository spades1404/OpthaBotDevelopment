import os
import tempfile

class Directories():
    def __init__(self):
        self.cwd = os.getcwd()
        self.assets = self.cwd + r"\Assets"

        #Asset directories
        self.currMod = self.cwd + r"\Class\ServerSide\currentModel.txt"
        self.OpthaBotLogo = self.assets + r"\opthabotlogo.png"
        self.icon = self.assets + r"\icon.png"
        self.emptyImageIcon = self.assets + r"\no-image-icon-6.png"
        self.model = self.assets +r"\model.h5"


        self.aeskey = self.assets + r"\key.key"
        self.configfilecrypted = self.assets + r"\config.txt"


        ''' Old stuff
        self.appConfigFile = self.assets + r"\configuration.json"
        self.appPermaSets = self.assets + r"\permaSet.json"
        self.configFile = self.assets + r"\dbkey1.json"
        self.keyFile = self.assets + r"\dbkey2.json"
        print(self.configfile)
        '''

    def makeTemp(self):
        self.temp = tempfile.mkdtemp()
        print(self.temp)

        self.configfile = self.temp + r"\config.txt"
        return self




if __name__ == "__main__":
    print("hi")
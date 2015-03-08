__author__ = 'Georgi @ 08.03.2015'
import wx
class windowCLass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowCLass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, "EXIT", "status msg")

        menuBar.Append(fileButton, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.SetTitle("Epic Window")
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
        app = wx.App() #new app, don't redirect stdout/stderr to a window
        windowCLass(None)
        app.MainLoop()



main()

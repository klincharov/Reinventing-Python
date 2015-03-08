__author__ = 'Georgi @ 08.03.2015'
import wx
import sys
class windowCLass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowCLass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)

        editButton = wx.Menu()
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT, "&Exit", "status msg")

        menuBar.Append(fileButton, "&File")
        menuBar.Append(editButton, "&Edit")

        nameBox = wx.TextEntryDialog(None, "What is your name ?", "Welcome", "name")

        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None, "Do you like wxPython", "Question", wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()


        wx.TextCtrl(panel, pos=(10,10), size=(250,150))

        if yesNoAnswer == wx.ID_NO:
            userName = "Loser"

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.SetTitle("Welcome " + userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()
        sys.exit()

def main():
        app = wx.App() #new app, don't redirect stdout/stderr to a window
        windowCLass(None)
        app.MainLoop()



main()

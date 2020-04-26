import Gui
import wx

if __name__ == "__main__":
    app = wx.App(False)
    frame = Gui.MyFrame(None)
    frame.Show(True)
    app.MainLoop()

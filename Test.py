#-------------------------------------------------------------------------------
# Name:        TextCtrlExampleFrame
# Purpose:
#
# Author:      ankier
#
# Created:     17/09/2012
# Copyright:   (c) ankier 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx

class TextCtrlExampleFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, \
         "Text ctrl example", pos =(0,0), size =(800, 600))
        panel = wx.Panel(self, -1)

        #多行文本样式
        self.text = wx.TextCtrl(panel, wx.ID_ANY,pos=(70, 0), size =(200, 60), style = wx.TE_MULTILINE)
        button = wx.Button(panel, wx.ID_ANY, pos = (210, 70), size =(100, 20), label = 'Append')
        button.Bind(wx.EVT_BUTTON, self.__OnAppendButtonClick)
        button = wx.Button(panel, wx.ID_ANY, pos = (110, 70), size =(60, 20), label = 'Clear')
        button.Bind(wx.EVT_BUTTON, self.__OnClearClick)

    def __OnAppendButtonClick(self, event):
        self.text.AppendText("appended text")
        print(self.text.GetValue())

    def __OnClearClick(self, event):
        self.text.Clear()


def main():
    app = wx.PySimpleApp()
    frame = TextCtrlExampleFrame()
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import hmm
import pickle

with open("init_pro_dict.pkl", "rb") as f:
    init_pros = pickle.load(f)
with open("biu_pro_dict.pkl", "rb") as f:
    biu_pros = pickle.load(f)
with open("change_pro_dict.pkl", "rb") as f:
    change_pros = pickle.load(f)
pages = 0
answer = []
prev_str = ''
waits = []


###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1300, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"待选字符区", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer3.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, pos=(-1, -1), size=(1100, -1))
        bSizer3.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"输入字符区", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer3.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY,  pos=(-1, -1), size=(1100, 150), style=wx.TE_MULTILINE)
        bSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        gbSizer2.Add(bSizer3, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALIGN_RIGHT, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"第1个词", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"第2个词", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"第3个词", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button12, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"第4个词", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"第5个词", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button14, 0, wx.ALL, 5)

        gbSizer2.Add(bSizer5, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.SetSizer(gbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_textCtrl3.Bind(wx.EVT_TEXT, self.input)
        self.m_button9.Bind(wx.EVT_BUTTON, self.nextpage)
        self.m_button10.Bind(wx.EVT_BUTTON, self.choose)
        self.m_button11.Bind(wx.EVT_BUTTON, self.choose)
        self.m_button12.Bind(wx.EVT_BUTTON, self.choose)
        self.m_button13.Bind(wx.EVT_BUTTON, self.choose)
        self.m_button14.Bind(wx.EVT_BUTTON, self.choose)

    def __del__(self):
        pass

    def input(self, event):
        global answer, prev_str, waits, pages
        pages = 0
        input_str = self.m_textCtrl3.GetValue()
        for i in range(len(input_str)):
            if input_str[i].encode('UTF-8').isalpha():
                break
        pinyin = ''.join(input_str[i:])
        prev_str = ''.join(input_str[0:i])
        # print(pinyin)
        answer = hmm.hmm(init_pros, change_pros, biu_pros, pinyin)
        # print(answer)
        wait = '      '
        waits = []
        for i in range(5):
            waits.append(answer[i])
        wait = wait.join(waits)
        self.m_textCtrl4.SetValue(wait)

    def nextpage(self, event):
        global pages, waits
        pages += 1
        wait = '      '
        waits = []
        end = pages*5+5
        if end < len(answer):
            for i in range(pages*5, end):
                waits.append(answer[i])
        else:
            for i in range(pages*5, len(answer)):
                waits.append(answer[i])
        wait = wait.join(waits)
        self.m_textCtrl4.SetValue(wait)

    def choose(self, event):
        x = event.GetEventObject()
        # print(x.GetLabel())
        index = int(x.GetLabel()[1])
        temp_str = waits[index-1]
        for i in range(len(temp_str)):
            if '\u4e00' <= temp_str[i] <= '\u9fff':
                break
        word = temp_str[i:]
        now_str = prev_str + word
        self.m_textCtrl3.SetValue(now_str)
        self.m_textCtrl4.Clear()














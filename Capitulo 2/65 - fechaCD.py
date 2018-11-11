import ctypes

ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
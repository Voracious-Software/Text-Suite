import ctypes

interfaceLib = ctypes.CDLL('Shared_Lib/bin/Library/libShared_Lib.so')

interfaceLib.test()
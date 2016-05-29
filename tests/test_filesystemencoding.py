#! /usr/bin/env py.test

import os
import sys

import py

pyexe = py.path.local(sys.executable)


def check_encoding():
    enc = pyexe.sysexec("ex-fsenc.py")
    print("ENC:", enc)
    file = py.path.local("dist/ex-fsenc")
    if os.path.isfile(file)
        enc_frozen = py.path.local("dist/ex-fsenc").sysexec()
        assert enc == enc_frozen
    except:
        print("File not found")


def test_getfilesystemencoding(monkeypatch):
    os.system("ccfreeze ex-fsenc.py")

    monkeypatch.setenv("LANG", "en_US.UTF-8")
    check_encoding()

    monkeypatch.setenv("LANG", "")
    check_encoding()

    monkeypatch.setenv("LANG", "de_AT@euro")
    check_encoding()

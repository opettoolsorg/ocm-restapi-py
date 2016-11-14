#!/usr/bin/env python

# package com.opet.utils

class Help:
  def __init__(self):
    pass

  def load(self, filepath):
    f = None
    file_contents = None
    try:
      f = open(filepath, 'r')
      file_contents = f.read()
    finally:
      if f is not None:
        f.close()

    return str(file_contents).strip()

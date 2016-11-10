#!/usr/bin/env python

# package com.opet.ocm.restapi

import json

from com.opet.ocm.restapi.Base import Base
from com.opet.ocm.restapi.dbcs import DBCS
from com.opet.ocm.restapi.ccs import CCS
 
# Facade
class restapi:
  factories={}
    'DBCS': DBCS.DBCS(), 
    'CCS': CCS.CCS()
  }
  def __init__(self, api_list):
    self.base=None
    self.valid_values="DBCS,CCS"
    restapi.__validate__(self,api_list)
    for i in range(len(api_list)):
      self.base=Base(api_list[i])

  def get(self,name):
    self.__check__(name)
    return restapi.factories[name]

  def toJson(self):
    return self.__str__()

  def __str__(self):
    retval=""
    if self.base is not None:
      retval=self.base.__str__()
    return retval

  def __check__(self,name):
    if name not in self.valid_values:
      raise NameError("Unsupported REST API: "+name)
    
  def __validate__(self, arg):
    if arg is None:
      raise NameError("Argument cannot be None: arg")
    elif isinstance(arg, list) == False:
      raise NameError("Argument must be a list")
    elif isinstance(arg[0], str) == False:
      raise NameError("Argument must be a str")
    else:
      for i in range(len(arg)):
        self.__check__(arg[i])

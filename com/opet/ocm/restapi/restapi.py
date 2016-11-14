#!/usr/bin/env python

# package com.opet.ocm.restapi

import json

from com.opet.ocm.restapi.Base import Base
 
# Facade
class restapi:
  factories={
    'DBCS': {'module_name': 'com.opet.ocm.restapi.dbcs.DBCS', 'instance': None}, 
    'CCS': {'module_name': 'com.opet.ocm.restapi.ccs.CCS', 'instance': None}
  }
  def __init__(self,interactive=False):
    self.base = None
    self.interactive = interactive
    self.valid_values = "DBCS,CCS"

  def register(self, api_list):
    restapi.__validate__(self, api_list)
    for i in range(len(api_list)):
      name = api_list[i]
      instance = restapi.factories[name]['instance']
      if instance is None:
        self.base=Base(name)

  def unregister(self, api_list):
    pass

  def use(self, name):
    retval = restapi.factories[name]['instance']
    if retval is None:
      retval = self.__load__(name)
      restapi.factories[name]['instance'] = retval
    return retval

  def list(self, name):
    return self.valid_values

  def help(self):
    from com.opet.utils.Help import Help
    import os
    help = Help.Help()
    return help.load(os.path.abspath(__file__)+'/restapi.help')

  def toJson(self):
    return self.__str__()

  def __str__(self):
    retval = ""
    if self.base is not None:
      retval = self.base.__str__()
    return retval

  def __load__(self, name):
    module = __import__(restapi.factories[name]['module_name'], fromlist = [name])
    clazz = getattr(module, name)
    return clazz()

  def __check__(self, name):
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
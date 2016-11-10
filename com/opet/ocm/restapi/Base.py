# package com.opet.ocm.restapi
#!/usr/bin/env python

# package com.opet.ocm.restapi

from collections import OrderedDict
import json

class Base:
  restapis = {'restapi' : []}
  def __init__(self, name):
    self.name = name
    api_list = Base.restapis['restapi']
    entry = OrderedDict()
    entry = {
      'tenant_users_password': None,
      'tenant_user': None,
      'tenant': None,
      'name': name
    }
    api_list.append(entry)

  def __setCommon__(self,name, tenant, tenant_user, tenant_users_password):
    api = self.__get__(name)
    api['tenant'] = tenant
    api['tenant_user'] = tenant_user
    api['tenant_users_password'] = tenant_users_password

  def __update__(self, name, key_name, key_value):
    api = self.__get__(name)
    api[key_name] = key_value

  def __remove__(self, name):
    api = self.__get__(name)
    del api

  def __get__(self, name):
    api_list = Base.restapis['restapi']
    api = None
    for i in range(len(api_list)):
      if api_list[i]['name'] == name:
        api = api_list[i]

    if api is None:
      raise NameError("No REST API registered with given name: "+name)

    return api
    
  def __str__(self):
    return json.dumps(Base.restapis)
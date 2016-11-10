#!/usr/bin/env python

# package com.opet.ocm.restapi.ccs

import requests

class Orchestrations:
  def __init__(self,logger,tenant,user,password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def list(self,container,authtoken):
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json'
    }
    r = requests.get(
      self.uri+'orchestration/'+container+'/public/', 
      headers=headers, 
      cookies=authtoken, 
      verify=False
    )
    return r.text

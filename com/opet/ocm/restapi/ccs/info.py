#!/usr/bin/env python

# package com.opet.ocm.restapi.ccs

import requests

class Info:
  def __init__(self,logger,tenant, user, password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def site(self,auth_token):
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json'
    }
    r = requests.get(
      self.uri+'/info/', 
      headers=headers, 
      cookies=auth_token, 
      verify=False
    )
    return r.text


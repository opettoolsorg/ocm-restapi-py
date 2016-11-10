#!/usr/bin/env python

# package com.opet.ocm.restapi.ccs

import requests

class Authentication:
  def __init__(self,logger,tenant, user, password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def getauthtoken(self):
    payload = { 'user' : self.tenant + '/' +self.tenant_user, 'password': self.tenant_users_password}
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json' 
    }
    auth_token=None
    r = requests.post(
      self.uri+'/authenticate/', 
      headers=headers, 
      json=payload, 
      verify=False
    )
    if r.status_code == 204:
      auth_token = r.cookies
    return auth_token

#!/usr/bin/env python

# package com.opet.ocm.restapi.ccs

import requests

class Quotas:
  def __init__(self,logger,tenant, user, password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def get(self,auth_token):
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json'
    }
    r = requests.get(
      self.uri+'/quota/'+self.tenant, 
      headers=headers, 
      cookies=auth_token, 
      verify=False
    )
    return r.text

  def discover(self,auth_token):
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json',
      'Accept': 'application/oracle-compute-v3+directory+json'
    }
    r = requests.get(
      self.uri+'/quota/'+self.tenant, 
      headers=headers, 
      cookies=auth_token, 
      verify=False
    )
    return r.text

  def list(self,auth_token):
    headers = {
      'Content-Type' : 'application/oracle-compute-v3+json'
    }
    r = requests.get(
      self.uri+'/quota/'+self.tenant+'/', 
      headers=headers, 
      cookies=auth_token, 
      verify=False
    )
    return r.text


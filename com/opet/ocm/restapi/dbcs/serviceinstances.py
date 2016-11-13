#!/usr/bin/env python

# package com.opet.ocm.restapi.dbcs

import requests

class ServiceInstances:
  def __init__(self,logger,tenant,user,password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def viewall(self):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/service/dbcs/api/v1.1/instances/'+self.tenant, 
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def viewcomputenodes(self,serviceId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/service/dbcs/api/v1.1/instances/'+self.tenant+'/'+serviceId+'/servers', 
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def viewoperationjobstatus(self,requestName,jobId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/service/dbcs/api/v1.1/instances/'+self.tenant+'/status/'+requestName+'/job/'+jobId, 
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

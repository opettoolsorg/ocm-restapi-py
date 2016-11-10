#!/usr/bin/env python

# package com.opet.ocm.restapi.dbcs

import requests

class Patches:
  def __init__(self,logger,tenant, user, password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self,args):
    self.__call__(args)

  def apply(self,serviceId,forceApply):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.put(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/patches/patchId?forceApply='+forceApply,
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.headers['Location']

  def precheckapplication(self,serviceId,patchId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/patches/checks/'+patchId,
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def rollback(self,serviceId,patchId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.delete(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/patches/'+patchId,
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def viewinformation(self,serviceId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/patches',
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text
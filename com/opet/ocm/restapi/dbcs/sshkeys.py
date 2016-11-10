#!/usr/bin/env python

# package com.opet.ocm.restapi.dbcs

import requests

class SSHKeys:
  def __init__(self,logger,tenant, user, password,uri):
    self.logger = logger
    self.tenant=tenant
    self.tenant_user=user
    self.tenant_users_password=password
    self.uri = uri

  def __call__(self):
    self.__call__()

  def viewselecteddetails(self,serviceId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/credentials/vmspublickey',
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def viewsummary(self,serviceId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/credentials/crednames/vmspublickey',
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def viewselectedsummaries(self):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/credentials/crednames',
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text

  def add(self,serviceId,public_key):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    payload = {
      'public-key': public_key 
    }
    r = requests.post(
      self.uri+'/paas/api/v1.1/instancemgmt/'+self.tenant+'/services/dbaas/instances/'+serviceId+'/credentials/crednames/vmspublickey',
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      json=payload, 
      verify=False
    )
    return r.headers['Location']

  def viewjobstatus(self,jobId):
    headers = {
      'Content-Type' : 'application/json',
      'X-ID-TENANT-NAME' : self.tenant 
    }
    r = requests.get(
      self.uri+'/paas/api/v1.1/activitylog/'+self.tenant+'/job/'+jobId,
      headers=headers, 
      auth=(self.tenant_user,self.tenant_users_password), 
      verify=False
    )
    return r.text
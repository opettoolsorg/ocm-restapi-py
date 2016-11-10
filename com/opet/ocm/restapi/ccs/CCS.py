#!/usr/bin/env python

# package com.opet.ocm.restapi.ccs

from com.opet.logging import logger
from com.opet.ocm.restapi.Base import Base
from com.opet.ocm.restapi.ccs import authentication, orchestrations, sshkeys, quotas
import json

class CCS(Base):
  def __init__(self):
    self.name="CCS"
    self.authentication=None
    self.orchestrations=None
    self.sshkeys=None
    self.quotas=None
  
  def setCommon(self, tenant, tenant_user, tenant_users_password, uri):
    Base.__setCommon__(self, self.name, tenant, tenant_user, tenant_users_password)
    Base.__update__(self, self.name, "uri", uri)
    self.authentication=authentication.Authentication(logger,tenant, tenant_user, tenant_users_password, uri)
    self.orchestrations=orchestrations.Orchestrations(logger,tenant, tenant_user, tenant_users_password, uri)
    self.sshkeys=sshkeys.SSHKeys(logger,tenant, tenant_user, tenant_users_password, uri)
    self.quotas=quotas.Quotas(logger,tenant, tenant_user, tenant_users_password, uri)

  def authentication(self):
    if self.authentication is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.authentication

  def orchestrations(self):
    if self.orchestrations is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.orchestrations

  def sshkeys(self):
    if self.sshkeys is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.sshkeys

  def quotas(self):
    if self.quotas is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.quotas

  def toJson(self):
    return Base.__str__(self)

  def __str__(self):
    obj = Base.__get__(self, self.name)
    return json.dumps(obj)
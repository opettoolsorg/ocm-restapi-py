#!/usr/bin/env python

# package com.opet.ocm.restapi.dbcs

from com.opet.logging import logger
from com.opet.ocm.restapi.Base import Base
from com.opet.ocm.restapi.dbcs import serviceinstances, sshkeys, patches
import json

class DBCS(Base):
  def __init__(self):
    self.name="DBCS"
    self.serviceinstances=None
    self.sshkeys=None
    self.patches=None

  def setCommon(self, tenant, tenant_user, tenant_users_password, uri):
    Base.__setCommon__(self, self.name, tenant, tenant_user, tenant_users_password)
    Base.__update__(self, self.name, "uri", uri)
    self.serviceinstances=serviceinstances.ServiceInstances(logger,tenant, tenant_user, tenant_users_password, uri)
    self.sshkeys=sshkeys.SSHKeys(logger,tenant, tenant_user, tenant_users_password,uri)
    self.patches=patches.Patches(logger,tenant, tenant_user, tenant_users_password,uri)

  def instances(self):
    if self.serviceinstances is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.serviceinstances

  def sshkeys(self):
    if self.serviceinstances is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.sshkeys

  def patches(self):
    if self.serviceinstances is None:
      raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
    return self.patches

  def toJson(self):
    return Base.__str__(self)

  def __str__(self):
    obj = Base.__get__(self, self.name)
    return json.dumps(obj)
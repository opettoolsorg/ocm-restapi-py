"""
DBCS.py
"""
#!/usr/bin/env python

# package com.opet.ocm.restapi.dbcs

import json

from com.opet.logging.logger import Logger
from com.opet.ocm.restapi.Base import Base
from com.opet.ocm.restapi.dbcs import serviceinstances, sshkeys, patches

class DBCS(Base):
    """
    DBCS
    """
    def __init__(self):
        Base.__init__(self, "DBCS")
        self.serviceinstances = None
        self.sshkeys = None
        self.patches = None

    def setCommon(self, tenant, tenant_user, tenant_users_password, uri):
        """
        Get serviceinstances object
        Args:
            tenant: String
            tenant_user: String
            tenant_users_password: String
            uri: String
        """
        Base.__setCommon__(self, tenant, tenant_user, tenant_users_password)
        Base.__update__(self, "uri", uri)
        logger = Logger()
        self.serviceinstances = serviceinstances.ServiceInstances(logger, tenant, tenant_user, tenant_users_password, uri)
        self.sshkeys = sshkeys.SSHKeys(logger, tenant, tenant_user, tenant_users_password, uri)
        self.patches = patches.Patches(logger, tenant, tenant_user, tenant_users_password, uri)

    def instances(self):
        """
        Get serviceinstances object
        """
        if self.serviceinstances is None:
            raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
        return self.serviceinstances

    def sshkeys(self):
        """
        Get sshkeys object
        """
        if self.serviceinstances is None:
            raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
        return self.sshkeys

    def patches(self):
        """
        Get patches object
        """
        if self.serviceinstances is None:
            raise NameError("You must call setCommon(self, tenant, tenant_user, tenant_users_password, uri) first!.")
        return self.patches

    def toJson(self):
        """
        Get JSON representation of DBCS object
        """
        return Base.__str__(self)

    def __str__(self):
        obj = Base.__get__(self)
        return json.dumps(obj)

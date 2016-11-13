Bourgeoiss-MacBook-Pro:~ opettools$ cd /Volumes/LaCie/u01/osc_ocm/tdbank-uc13
Bourgeoiss-MacBook-Pro:tdbank-uc13 opettools$ export PYTHONPATH=`pwd`/pytz-2010h:`pwd`/requests-2.11.1:`pwd`/jsonpath-0.54:`pwd`/inventory-reporting/python
Bourgeoiss-MacBook-Pro:inventory-reporting opettools$ python
Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from com.opet.ocm.restapi import restapi
>>> factory = restapi.restapi()
>>> factory.register("DBCS","CCS"])
>>> dbcs = factory.use("DBCS")
>>> dbcs.setCommon("tenant5","t5admin","t3nant-5","https://ocm14-psm-vip.us.osc.oracle.com")
>>> ccs = factory.use("CCS")
>>> ccs.setCommon("tenant5","t5user","t3nant-5","https://ocm14api.us.osc.oracle.com")
>>> print factory.toJson()
{"restapi": [{"tenant_users_password": "t3nant-5", "uri": "https://ocm14-psm-vip.us.osc.oracle.com", "tenant_user": "t5admin", "tenant": "tenant5", "name": "DBCS"}, {"tenant_users_password": "t3nant-5", "uri": "https://ocm14api.us.osc.oracle.com", "tenant_user": "t5user", "tenant": "tenant5", "name": "CCS"}]}
>>> dbcs.sshkeys.viewselecteddetails("AD-INTEG")
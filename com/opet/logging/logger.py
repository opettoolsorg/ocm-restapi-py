#!/usr/bin/env python

# package com.opet.logging

import sys
import os
import datetime
import pytz 
from pytz import timezone

SEVERITY_LEVEL=None
TZ='US/Pacific'

def getSeverityName(search_var):
  retval="UNKNOWN"

  if search_var == 0:
    retval="ERROR"
  elif search_var == 1:
    retval="WARN"
  elif search_var == 2:
    retval="INFO"
  elif search_var == 3:
    retval="TRACE"
  return retval

def setSeverityLevel(level):
  global SEVERITY_LEVEL

  _tmp=getSeverityName(level)
  if _tmp == "UNKNOWN":
    log("INFO","setSeverityLevel","Invalid argument specified: " + level)
  else:
    SEVERITY_LEVEL=level

  log("INFO","setSeverityLevel","SEVERITY_LEVEL=" + getSeverityName(SEVERITY_LEVEL))

def getSeverityLevel():
  global SEVERITY_LEVEL
  return getSeverityName(SEVERITY_LEVEL)

def setTimezone(tzname):
  global TZ
  TZ = tzname
  log("INFO","setTimezone","TZ=" + tzname)

def getTimezone():
  global TZ
  return TZ

def log(severity,function_name,message):
  global SEVERITY_LEVEL
  global TZ

  if severity == "ERROR":
    _SL=0
  elif severity == "WARN":
    _SL=1
  elif severity == "INFO":
    _SL=2
  elif severity == "TRACE":
    _SL=3
  else:
    _SL=99

  if _SL <= SEVERITY_LEVEL:
    print "%s %s <%s> %s" % (datetime.datetime.now(timezone(TZ)).strftime("%a %b %d %H:%M:%S %Z %Y"),severity,function_name,message)

def main():
  global SEVERITY_LEVEL
  log("INFO","logging","OPET_LOGGING_SEVERITY_LEVEL=" + os.environ.get('OPET_LOGGING_SEVERITY_LEVEL'))
  # 0=ERROR,1=WARN,2=INFO,3=TRACE
  SEVERITY_LEVEL=os.getenv('OPET_LOGGING_SEVERITY_LEVEL',2)

if __name__ == "__main__":
  main()

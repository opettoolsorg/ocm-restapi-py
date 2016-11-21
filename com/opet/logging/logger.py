"""
logger.py
"""

#!/usr/bin/env python

# package com.opet.logging

import os
import datetime

from pytz import timezone

class Logger(object):
    """
    Logger
    """
    def __init__(self):
        self._severity_level = None
        self._tz = 'US/Pacific'

    def getSeverityName(self, level):
        """
        Get severity name associated with a given severity level
        Args:
            level: Number associated with severity level

        Returns:
            String
        """
        retval = 'UNKNOWN'

        if level == 0:
            retval = "ERROR"
        elif level == 1:
            retval = "WARN"
        elif level == 2:
            retval = "INFO"
        elif level == 3:
            retval = "TRACE"
        return retval

    def setSeverityLevel(self, level):
        """
        Set severity level to specified value
        Args:
            level: Number associated with severity level

        """
        _tmp = self.getSeverityName(level)
        if _tmp == "UNKNOWN":
            self.log("INFO", "setSeverityLevel", "Invalid argument specified: " + level)
        else:
            self._severity_level = level

        self.log(
            "INFO",
            "setSeverityLevel",
            "severity_level=" + self.getSeverityName(self._severity_level))

    def getSeverityLevel(self):
        """
        Get name associated with current severity level
        Returns:
            String
        """
        return self.getSeverityName(self._severity_level)

    def setTimezone(self, tzname):
        """
        Set timezone to specified value
        Args:
            _tzname: String associated with timezone
        """
        self._tz = tzname
        self.log("INFO", "setTimezone", "_tz=" + tzname)

    def getTimezone(self):
        """
        Get current timezone
        Returns:
            String
        """
        return self._tz

    def log(self, severity, function_name, message):
        """
        Log a message for the specified function, using the specified severity
        Args:
            severity: Name of severity level
            function_name: Name of function or function signature
            message: Message to log
        """
        if severity == "ERROR":
            _sl = 0
        elif severity == "WARN":
            _sl = 1
        elif severity == "INFO":
            _sl = 2
        elif severity == "TRACE":
            _sl = 3
        else:
            _sl = 99

        if _sl <= self._severity_level:
            print "%s %s <%s> %s" % (
                datetime.datetime.now(timezone(self._tz)).strftime("%a %b %d %H:%M:%S %Z %Y"),
                severity, function_name, message)

    def main(self):
        """
        main
        """
        logger = Logger()
        logger.log(
            "INFO",
            "logging",
            "OPET_LOGGING__severity_level=" + os.environ.get('OPET_LOGGING__severity_level')
        )
        # 0=ERROR,1=WARN,2=INFO,3=TRACE
        logger.setSeverityLevel(os.getenv('OPET_LOGGING__severity_level', 2))

        if __name__ == "__main__":
            self.main()

# -*- encoding: utf-8 -*-

from datetime import datetime

PYSIS_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

def convertToDateTime(dt):
    """Converts a string to a datetime
    
    Args: dt (int, str, datetime): A form of a datetime
        int - UTC time
        str - datetime in the TZ format
        datetime - no conversion needed, just returns it
    
    Returns:
        DateTime object
    """
    
    if dt is not None:
        if isinstance(dt, datetime):
            pass
        elif isinstance(dt, str):
            dt = datetime.strptime(dt, PYSIS_DATE_FORMAT)
        elif isinstance(dt, int):
            dt = datetime.utcfromtimestamp(dt)
        else:
            raise ValueError('Value must be a datetime or string type')
    
    return dt
            
    
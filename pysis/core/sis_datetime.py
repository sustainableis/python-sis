from datetime import datetime

PYSIS_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

def convertToDateTime(dt):
    
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
            
    
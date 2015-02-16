from pysis import SIS
from pysis.exceptions import BadRequest

if __name__ == "__main__":
    s = SIS(token="891fea6456f40f6369b824fb0a8ddcf0d983096f",
            enableParamChecks=False)
    
    output = s.outputs.get(91)
    
    try:
        data = output.getData(timeStart=1412117100,
                              timeEnd=1412120700,
                              window=45)
    except BadRequest as ex:
        print(str(ex) + "\nBadRequest - OK")
    
    
    
    

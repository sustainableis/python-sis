from pysis import SIS

if __name__ == "__main__":
    s = SIS(token="891fea6456f40f6369b824fb0a8ddcf0d983096f",
            enableParamChecks=False)
    
    #outputs = s.outputs.get(facility_id=102)
    #for output in outputs:
    #    print(str(output.id) + ' : ' + output.label + ' : ' + output.created_at)
    
    output = s.outputs.get(91)
    #fields = output.getFields()
    
    #for field in fields:
    #    print(field.field_human_name)
    
    #data = output.getData(timeStart=1401451200)
    #data = output.getData(timeStart='2014-09-30T23:45:00.000Z')
    output = s.outputs.get(91)
    data = output.getData(timeStart=1412117100,
                          timeEnd=1412120700,
                          window=0)
    
    #data = output.getData(timeStart=1412117100,
    #                      timeEnd=1412120700,
    #                      window=3600,
    #                      fields=['DefrostMinutesSetp', 'NH3_Reading'])
    
    #for d in data:
    #    print(d._attrs)
        
    #data = output.getData()
    for d in data:
        print(d._attrs)
            

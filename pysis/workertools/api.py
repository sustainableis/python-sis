import os,sys
from datetime import datetime
import datetime as DT
import boto3
from psycopg2 import IntegrityError


class APIFileSaver:


    def __init__(self, apiDBConnection, accessKeyID=None, secretAccessKey=None):
        self.s3 = None
        self.psql = apiDBConnection
        self.systemUserID = 18
        self.accessKeyID = accessKeyID
        self.secretAccessKey = secretAccessKey

    def initS3(self):
        self.s3 = boto3.client('s3', aws_access_key_id=self.accessKeyID, aws_secret_access_key=self.secretAccessKey)

    def saveFile(self, fileName, file_category_id, local_filepath, description='', facility_id=None, organization_id=None, content_type='', superuser_required=False):
        apiFile = APIBackedFile()
        if self.s3 is None:
            self.initS3()

        return apiFile.save(self.s3, self.psql, self.systemUserID, fileName, file_category_id, local_filepath, description, facility_id, organization_id, content_type, superuser_required)
    


class APIBackedFile:

    S3_BUCKET = 'sis-api-production'

    def __init__(self):
        pass
    

    def save(self, s3Connection, s3bucket, psqlConnection, created_by, fileName, file_category_id, local_filepath, description='', facility_id=None, organization_id=None, content_type='', superuser_required=False):
        base_filename = os.path.basename(fileName)
        print ('Uploading local file: ' + str(local_filepath))


        s3Connection.upload_file(local_filepath, APIBackedFile.S3_BUCKET, fileName)


        return_id = None
        try:
            query = "select * from files where filename ='%s' order by version DESC limit 1"%(k.key)
            existing_files = psqlConnection.complicatedSelectExecution(query, dictResults=True)
            if len(existing_files) > 0:
                version = int(existing_files[0]['version']) + 1
            else:
                version = 1
            
            return_id = psqlConnection.insertOne("files", {'filename': k.key,
                                               'base_filename': base_filename,
                                               'description' : description,
                                               'content_type' : content_type,
                                               'status': "ACTIVE",
                                               'superuser_required' : superuser_required,
                                               'version' : version,
                                               'file_category_id': file_category_id,
                                               'created_by' : created_by,
                                               'updated_at' : datetime.now()
                                             })
            if facility_id is not None:
                psqlConnection.insertOne("facility_files", { 'facility_id' : facility_id,
                                                             'file_id' : return_id
                                                           }, returning="facility_id")
            if organization_id is not None:
                psqlConnection.insertOne("organization_files", {'organization_id': organization_id,
                                                                'file_id': return_id
                                                            })
        except IntegrityError as ie:
            print ('ERROR: File already exists! Skipping')
            return_id = None
        
        return return_id
        
  
    def trackProgress(self, complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()
        if complete == total:
            print ('')

class RateScheduleCalculationException(Exception):
  pass


class APIRateSchedule():
  
    def __init__(self, psql, schedule_id):
        self.psql = psql
        self.schedule_id = schedule_id
        self.schedule = []
    
    def getRateSchedule(self):
        query = 'select * from rate_seasons inner join rate_season_periods rsp on rsp.rate_season_id=rate_seasons.id inner join usage_tier_rates utr on utr.rate_season_period_id=rsp.id  where rate_schedule_id=%s'%(self.schedule_id)
        rows = self.psql.complicatedSelectExecution(query, dictResults=True)
        for row in rows:
            self.schedule.append(row)
                
                
    def rateTiersForDateAndValue(self, date, usageValue):
        month = date.month
        day = date.day
        weekday = date.weekday()
        hour = date.hour
      
        matchedSchedule = None
        for schedule in self.schedule:
            if not (month <= schedule['end_month'] and month >= schedule['start_month']):
                continue
            if not (day <= schedule['end_day'] and day >= schedule['start_day']):
                continue
            if not (weekday <= schedule['day_of_week_end'] and weekday >= schedule['day_of_week_start']):
                continue
            if not (hour < schedule['hour_end'] and hour >= schedule['hour_start']):
                continue
            if not (usageValue <= schedule['unit_stop_value'] and usageValue >= schedule['unit_start_value']):
                continue
        
            if matchedSchedule is not None:
                raise RateScheduleCalculationException('More that one matched schedule!')
            matchedSchedule = schedule
      
            if matchedSchedule is None:
                raise RateScheduleCalculationException('No matched schedule!')
        return matchedSchedule
    
    def rateTiersForDate(self, date):
        month = date.month
        day = date.day
        weekday = date.weekday()
        hour = date.hour
      
        matchedScheduleWithTiers = []
        for schedule in self.schedule:
            scheduleStartDate = DT.date(date.year, schedule['start_month'], schedule['start_day'])
            scheduleEndDate = DT.date(date.year, schedule['end_month'], schedule['end_day'])
            if not (scheduleStartDate <= date <= scheduleEndDate):
                continue
            if not (weekday <= schedule['day_of_week_end'] and weekday >= schedule['day_of_week_start']):
                continue
            if not (hour < schedule['hour_end'] and hour >= schedule['hour_start']):
                continue
    
            matchedScheduleWithTiers.append(schedule)
      
        if len(matchedScheduleWithTiers) == 0:
            raise RateScheduleCalculationException('No matched schedules!')
        return matchedScheduleWithTiers
    
    def ratesForSingleDay(self,date, usageValue):
        month = date.month
        day = date.day
        weekday = date.weekday()
            
        matchedSchedules = []
        for schedule in self.schedule:
            scheduleStartDate = DT.date(date.year, schedule['start_month'], schedule['start_day'])
            scheduleEndDate = DT.date(date.year, schedule['end_month'], schedule['end_day'])
            if not (scheduleStartDate <= date <= scheduleEndDate):
                continue
            if not (weekday <= schedule['day_of_week_end'] and weekday >= schedule['day_of_week_start']):
                continue
            if not (usageValue <= schedule['unit_stop_value'] and usageValue >= schedule['unit_start_value']):
                continue
        
            matchedSchedules.append(schedule)
        if len(matchedSchedules) == 0:
            raise RateScheduleCalculationException('No matched schedules!')
        return matchedSchedules

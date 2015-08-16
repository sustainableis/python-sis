from impala.dbapi import connect
from pysis.workertools.baseWorker import BaseWorker





class BaseLineageWMSWorker(BaseWorker):
    
    
    
    def __init__(self, workerUUID, environment):
        
        super(BaseLineageWMSWorker, self).__init__(workerUUID, environment)
        
        self.impalaConfig = {'host': self.config['impala_host'],
                             'port': self.config['impala_port'],
                             'db': self.config['impala_db']};
                             
        self.conn = connect(host=self.impalaConfig['host'],
                            port=self.impalaConfig['port'],
                            database=self.impalaConfig['db']);
                            
                            
                            

        
        
    
    
        
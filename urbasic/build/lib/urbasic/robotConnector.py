'''
Python 3.x library to control an UR robot through its TCP/IP interfaces
Copyright (C) 2017  Martin Huus Bjerge, Rope Robotics ApS, Denmark

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL "Rope Robotics ApS" BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of "Rope Robotics ApS" shall not be used
in advertising or otherwise to promote the sale, use or other dealings in this Software
without prior written authorization from "Rope Robotics ApS".
'''
__author__ = "Martin Huus Bjerge"
__copyright__ = "Copyright 2017, Rope Robotics ApS, Denmark"
__license__ = "MIT License"

import urbasic
#import URplus #import if any UPplus modules is needed

class RobotConnector(object):
    '''
    Class to hold all connection to the Universal Robot and plus devises

    Input parameters:

    '''


    def __init__(self, robotModel, host : str, hasForceTorque : bool = False, conf_filename : str | None = None):
        '''
        Constructor see class description for more info.
        '''
        if(False):
            assert isinstance(
                robotModel, urbasic.robotModel.RobotModel
            )  ### This line is to get code completion for RobotModel
        self.RobotModel = robotModel
        self.RobotModel.ipAddress = host
        self.RobotModel.hasForceTorqueSensor = hasForceTorque
        self.RealTimeClient = urbasic.realTimeClient.RealTimeClient(robotModel)
        self.DataLog = urbasic.dataLog.DataLog(robotModel)
        self.RTDE = urbasic.rtde.RTDE(robotModel, conf_filename=conf_filename)
        self.DashboardClient = urbasic.dashboard.DashBoard(robotModel)
        self.ForceTourqe = None
        # if hasForceTorque:
        #     self.ForceTourqe = URplus.forceTorqueSensor.ForceTorqueSensor(robotModel)

        logger = urbasic.dataLogging.DataLogging()
        name = logger.AddEventLogging(__name__)
        self.__logger = logger.__dict__[name]
        self.__logger.info('Init done')


    def close(self):
        try:
            self.RealTimeClient.Disconnect()
        except:
            pass
        self.RealTimeClient = None
        try:
            self.RTDE.close()
        except:
            pass
        self.RTDE = None
        try:
            self.DashboardClient.close()
        except:
            pass
        self.DashboardClient = None
        try:
            if self.ForceTourqe is not None:
                self.ForceTourqe.close()
                self.ForceTourqe = None
        except:
            pass
        try:
            self.DataLog.close()
        except:
            pass
        self.DataLog = None

import datetime
import time

from wateringcan import WateringCan
import helpers


class Gardener(object):

    # watering_time_hours = [22, 4]
    watering_time_hours = None
    # rest_time_hours = 0.9
    rest_time_hours = 0.0015  # =5.4s
    # single_watering_time_sec = 60
    single_watering_time_sec = 15

    def __init__(self, watering_can=None, rest_time_hours=None, single_watering_time_sec=None):
        if watering_can is not None:
            self.watering_can = watering_can
        else:
            self.watering_can = WateringCan()
        if rest_time_hours is not None:
            self.rest_time_hours = rest_time_hours
        if single_watering_time_sec is not None:
            self.single_watering_time_sec = single_watering_time_sec

    def set_watering_time_hours(self, watering_time_hours):
        self.watering_time_hours = watering_time_hours

    @helpers.garden_log
    def take_care_of_garden(self):
        if self.is_it_time_for_watering():
            watering = self.watering_can.start_watering()
            if watering is True:
                time.sleep(self.single_watering_time_sec)
            self.watering_can.stop_watering()

    @helpers.garden_log
    def is_it_time_for_watering(self):
        if self.watering_time_hours is None:
            return True
        now = datetime.datetime.now()
        if now.hour in self.watering_time_hours:
            return True
        else:
            return False

    @helpers.garden_log
    def get_rest(self, hours=None):
        """Sleep for some time"""
        if hours is not None:
            time.sleep(int(60*60*hours))
        else:
            time.sleep(int(60*60*self.rest_time_hours))


def main():
    gardener = Gardener()
    while True:
        gardener.take_care_of_garden()
        gardener.get_rest()


if __name__ == "__main__": main()

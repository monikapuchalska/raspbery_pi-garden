import datetime
import random
import pump
import helpers

@helpers.garden_log
def is_it_dry():
    """Check if soil is dry."""
    # return random.choice([True, False])
    if pump.is_humid() == 0:
        return True
    else:
        return False


class WateringCan(object):
    """Watering can """

    last_successful_watering_time = None
    number_of_failures = 0
    acceptable_failures = 3

    def __init__(self, acceptable_failures=None):
        if acceptable_failures is not None:
            self.acceptable_failures = acceptable_failures

    @helpers.garden_log
    def start_watering(self):
        """Turn on the pump."""
        if self.number_of_failures >= self.acceptable_failures:
            raise Exception('Too many failed waterings - can might be empty')
        if is_it_dry():
            pump.pump(True)
            return True
        else:
            self.save_successful_watering()
            return False

    @helpers.garden_log
    def stop_watering(self):
        """Turn off the pump."""
        pump.pump(False)

        if is_it_dry():
            self.save_failed_watering()
        else:
            self.save_successful_watering()
        return True

    @helpers.garden_log
    def save_successful_watering(self):
        self.last_successful_watering_time = datetime.datetime.now()
        self.number_of_failures = 0

    @helpers.garden_log
    def save_failed_watering(self):
        self.number_of_failures += 1

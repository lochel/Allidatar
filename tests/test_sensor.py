from allidatar import Sensor

def test_sensor():
  sensor = Sensor()
  sensor.start()
  sensor.stop()
  # If no exceptions are raised, the test passes
  assert True

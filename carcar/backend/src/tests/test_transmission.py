from backend.src.components.transmission import ManualTransmission, AutomaticTransmission


def test_manual_transmission():
    transmission = ManualTransmission()
    assert transmission.get_gear() == 1
    transmission.shift_up()
    assert transmission.get_gear() == 2
    transmission.shift_down()
    assert transmission.get_gear() == 1
    transmission.shift_down()
    assert transmission.get_gear() == 1


def test_automatic_transmission():
    transmission = AutomaticTransmission()
    assert transmission.get_gear() == 1
    transmission.shift_up()
    assert transmission.get_gear() == 2
    transmission.shift_down()
    assert transmission.get_gear() == 1
    transmission.shift_down()
    assert transmission.get_gear() == 1

import usb.core
import usb.util

# find our device
# dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)
# dev = usb.core.find(idVendor=0x046D, idProduct=0x0836)
devs = usb.core.find(find_all=True)
# dev2 = usb.core.find(idVendor=0x046D, idProduct=0x081B)

for dev in devs:
    # print(dev.__str__())
    print(dev.address, dev.port_number, dev.manufacturer, dev.product, dev.bus, dev.serial_number, dev.bDeviceClass)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')
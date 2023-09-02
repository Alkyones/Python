import asyncio
from winsdk.windows.devices import radios


async def bluetooth_power(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if this_radio.state == 2:
                result = await this_radio.set_state_async(radios.RadioState.ON)
                print("Bluetooth ON")
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)
                print("Bluetooth OFF")
if __name__ == '__main__':
    asyncio.run(bluetooth_power(False))
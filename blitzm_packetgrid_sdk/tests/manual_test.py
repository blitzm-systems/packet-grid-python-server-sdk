from blitzm_packetgrid_sdk import Recipient, SendNotification, TransportEnum
from blitzm_packetgrid_sdk.services.packetgrid import PacketGrid
import os


def run():
    tenant_id = os.environ.get('tenant-id')
    api_key = os.environ.get('api-key')
    is_production = True
    packet_grid = PacketGrid(tenant_id, api_key, is_production)
    recipient = Recipient(username='Recipient-username',
                          email='Recipient-email',
                          phone='Recipient-phone-number')
    notification = SendNotification(title='Your-message-title',
                                    detail='Hello from PacketGrid',
                                    recipients=[recipient],
                                    transports=[TransportEnum.EMAIL, TransportEnum.SMS],
                                    payload={})
    packet_grid.notifications.send(notification)


if __name__ == "__main__":
    run()

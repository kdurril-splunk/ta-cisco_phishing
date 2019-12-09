import json

from splunklib.modularinput import *


class CiscoMessageProcessor:

    def __init__(self, checkpoint):
        self._checkpoint = checkpoint

    def save_messages(self, messages, input_name, ew):
        for data in messages:
            if data is not None and data['messages'] != "" and len(data['messages']) > 0:
                ew.log('INFO', 'Cisco phishing data input is processing page: ' + str(data['offset']))
                for message in data['messages']:
                    # Create an Event object, and set its fields
                    ev = Event()
                    ev.stanza = input_name
                    ev.time = message['date']
                    ev.data = json.dumps(message)

                    # Tell the EventWriter to write this event
                    ew.write_event(ev)
                    last_processed_time = message['date']

        # save the checkpoint after each event is written to avoid duplication
        self._checkpoint.update_checkpoint(last_processed_time)

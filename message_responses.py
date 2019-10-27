from chat_functions import send_text_to_room
import logging
import re

logger = logging.getLogger(__name__)


class Message(object):

    def __init__(self, client, store, config, message_content, room, event):
        """Initialize a new Message

        Args:
            client (nio.AsyncClient): nio client used to interact with matrix

            store (Storage): Bot storage

            config (Config): Bot configuration parameters

            message_content (str): The body of the message

            room (nio.rooms.MatrixRoom): The room the event came from

            event (nio.events.room_events.RoomMessageText): The event defining the message
        """
        self.client = client
        self.store = store
        self.config = config
        self.message_content = message_content
        self.room = room
        self.event = event

        self.season_episode_regex = re.compile(r"s(\d+)e(\d+)", flags=re.IGNORECASE)

    async def process(self):
        """Process and possibly respond to the message"""
        response = ""

        # Check if there was a SXXEXX mention in the message
        for match_group in self.season_episode_regex.finditer(self.message_content):
            # Extract the season and episode numbers
            season, episode = (int(match_group.group(1)), int(match_group.group(2)))
            logger.info("Searching for season %d, episode %s", season, episode)

            # Return the link to the mentioned episode
            try:
                ep = self.config.episodes[season][episode]
                title = ep["name"]
                link = ep["link"]
                logger.info("Found %s from season/episode combo", title)
            except KeyError:
                continue

            response += "%s: %s" % (title, link)

        # Check for episode titles in the message
        for title, link in self.config.episode_titles_to_link.items():
            if title.lower() in self.message_content.lower():
                logger.info("Found title in message: %s", title)
                response += "%s: %s" % (title, link)

        if response:
            await send_text_to_room(self.client, self.room.room_id, response)

# Warning: This code is very old and there are better ways to make Matrix bots in Python these days. I recommend you check out either [maubot](https://github.com/maubot/maubot) (easy) or [mautrix-python](https://github.com/mautrix/python) (for something more low-level).

# Matrix Episode Bot

A bot for sending links to episodes mentioned in a chat room.

## Setup

Copy `sample.config.yaml` to `config.yaml` and edit to your needs. See the
`example_configs` directory for examples.

## Usage

Users should be able to get a link to browse episodes with `!episodes list`.
This text is configurable in `config.yaml`.

Otherwise any time an episode title is mentioned in a message, or a
season/episode combo in the form of `S02E05` (for Season 2, Episode 5 of the
show), then the bot will post the name of an episode and a link to watch it.

## Questions?

Any questions? Ask in
[#episode-bot:amorgan.xyz](https://matrix.to/#/!vUFgYAKqpITnhFvYoS:amorgan.xyz?via=amorgan.xyz&via=matrix.org)!

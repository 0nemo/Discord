def command(msg, message):
  if msg.lower() == "ping":
    await message.channel.send("pong")
VirtualHost "guest.aparkinson.net"
    authentication = "anonymous"

Component "chat-muc.aparkinson.net" "muc"
    name = "Test chat room server yay! :D"
    restrict_room_creation = "admin"
    admins = { "woodhouse@aparkinson.net" }

    disco_hidden = true


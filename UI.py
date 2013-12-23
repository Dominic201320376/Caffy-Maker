from CC import create, login, delete, logout
from Main import messages, status, friends
while True:
    choice = raw_input("What do you want to do? (C - Create, L - Login, D - Delete, Q - Quit) ")
    choice = choice.lower()
    if choice == 'c':
        c = create()
        c.ask_name()
        c.ask_password()
        c.create()
    elif choice == 'l':
        l = login()
        if l.login() == 1:
            name = l.get_name()
            while True:
                choice = raw_input("What do you want to do? (M - Messages, S - Status, F - Friends, L - Logout) ")
                choice = choice.lower()
                if choice == 'm':
                    m = messages()
                    while True:
                        m.get_messages(name)
                        m.print_messages()
                        choice = raw_input("What do you want to do? (S - Send Message, R - Return) ")
                        choice = choice.lower()
                        if choice == 's':
                            m.send_message(name)
                        elif choice =='r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 's':
                    s = status()
                    while True:
                        s.print_status()
                        choice = raw_input("What do you want to do? (C - Create Status, R - Return) ")
                        choice = choice.lower()
                        if choice == 'c':
                            s.create_status()
                            s.status_export(name)
                        elif choice == 'r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 'f':
                    f = friends()
                    f.set_name(name)
                    while True:
                        print "Friends:"
                        f.see_friends(name)
                        print "Friend Requests (Recieved, Sent):"
                        f.see_friend_requests(name)
                        choice = raw_input("What do you want to do? (A - Add Friend, D - Delete Friend, F - Approve Friend Request, R - Return) ")
                        choice = choice.lower()
                        if choice == 'a':
                            f.add_friend(name)
                        elif choice == 'd':
                            f.delete_friends(name)
                        elif choice == 'f':
                            f.approve_request(name)
                        elif choice == 'r':
                            break
                        else:
                            print "Invalid input"
                elif choice == 'l':
                    l = logout()
                    l.exit()
                    break
                else:
                    print "Invalid input"
        else:
            print "Username/Password is invalid"
    elif choice == 'd':
        d = delete()
    elif choice == 'q':
        break
    else:
        print "Invalid input"
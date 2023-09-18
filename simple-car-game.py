command = ""
started = False
while command.lower() != "quit":
    command = input("> ")
    if command == 'start':
        if started:
            print("car is already started")
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print("car stopped")
    elif command == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command == 'quit':
        break
    else:
        print('Unknown character. type help for assistance.')
        break
        

        
        
        
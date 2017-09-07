def controllerActionCount(controller_name):
    f = open('development1.log')
    lines = f.readlines()
    f.close()

    controller_counter = 0
    index_counter = 0
    show_counter = 0
    update_counter = 0
    login_counter = 0
    create_counter = 0

    for line in lines:
        line_list = line.split()
        if 'Processing by'.lower() in line.lower():
            if controller_name.lower() in line_list[2].lower():
                controller_counter += 1
                controller_name_action = line_list[2].split('#')
                if controller_name_action[1].lower() == 'index':
                    index_counter += 1
                if controller_name_action[1].lower() == 'show':
                    show_counter += 1
                if controller_name_action[1].lower() == 'update':
                    update_counter += 1
                if controller_name_action[1].lower() == 'login':
                    login_counter += 1
                if controller_name_action[1].lower() == 'create':
                    create_counter += 1

    result = '{0} occurred {1} times and methods ran:\nindex - {2}\nshow - {3}\nupdate - {4}\nlogin - {5}\n' \
             'create - {6}'.format(controller_name,
                                   controller_counter,
                                   index_counter,
                                   show_counter,
                                   update_counter,
                                   login_counter,
                                   create_counter
                                   )
    print(result)


controller = 'SprintsController'
controllerActionCount(controller)

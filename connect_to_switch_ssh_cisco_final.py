from netmiko import ConnectHandler


# Создание словаря с параметрами подключения к коммутатору
# Необходимо указать свои параметры
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.1',
    'username': 'username',
    'password': 'password',
    'port': 22,
    'secret': 'enable_password'
}

# Подключение к коммутатору
ssh_connect = ConnectHandler(**device)

# Вход в режим enable
ssh_connect.enable()

commands = ['show version',
            'show startup-config',
            'show running-config',
            'show ip access-list',
            'show interface']

# Отправка команд
for command in commands:
    print(command)
    output = ssh_connect.send_command(command)
    if command == 'show version':
        start_index = output.find('Version ') + len('Version ')
        end_index = output.find(',', start_index)
        version = output[start_index:end_index]

        # Запись результата в файл
        filename = 'results_of_commands.txt'
        with open(filename, 'w') as f:
            f.write('Command: ' + command + '\n\n' +
                    'Result:' + '\n\n' + 'Version: ' +
                    version + '\n\n________________________________\n\n')
    else:

        # Запись результата в файл
        filename = 'results_of_commands.txt'
        with open(filename, 'a') as f:
            f.write('Command: ' + command + '\n\n' +
                    'Result:' + '\n\n' + output +
                    '\n\n________________________________\n\n')

# Закрытие подключения
ssh_connect.disconnect()

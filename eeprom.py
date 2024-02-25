import sys
import serial

def convert_number(n):
    numero = int(n)
    # Converter o número para uma string de bytes
    string_bytes = numero.to_bytes(2, byteorder='little')
    # Preencher a string de bytes para ter 4 bytes
    string_bytes += b'\x00' * (2 - len(string_bytes))
    return string_bytes

def read_eeprom(start_addr, size):
    ser.write(b'r' + convert_number(start_addr) + convert_number(size))
    ser.flush()
    line = ser.readline()
    print("response=", line)

def write_eeprom(start_addr, size, data):
    ser.write(b'w' + convert_number(start_addr) + convert_number(size) + data)
    ser.flush()
    line = ser.readline()
    print("response=", line)

def load_file_content(filename, size):
    with open(filename, 'rb') as arquivo:
        # Ler todos os bytes do arquivo
        bytes_lidos = arquivo.read(size)

    # Converter os bytes para uma string onde cada caractere representa 1 byte
    #string_bytes = ''.join([chr(byte) for byte in bytes_lidos])
    return bytes_lidos

#---------------- start program here-----------------------

# Verifica se foram fornecidos os dois argumentos esperados
if len(sys.argv) != 3:
    print("uso: python eeprom.py <nome_do_arquivo> <tamanho>")
    sys.exit(1)

# Obtém os argumentos da linha de comando
nome_arquivo = sys.argv[1]
tamanho_arquivo = int(sys.argv[2])


# pegar o conteudo do arquivo
file_content = load_file_content(nome_arquivo, tamanho_arquivo)
size_in_bytes = len(file_content)

# inicia comunicacao serial com arduino
ser = serial.Serial('COM5', 57600)  # open serial port
print(ser.name)             # check which port was really used

line = ser.readline()
print("response=", line)
write_eeprom(0, tamanho_arquivo, file_content)

line = ser.readline()
print("response=", line)
read_eeprom(0, tamanho_arquivo)

ser.close()                 # close port

from pydub import AudioSegment
import struct

def hide_data_in_mp3(input_file, output_file, secret_message):
    audio = AudioSegment.from_mp3(input_file)
    
    binary_message = ''.join(format(ord(c), '08b') for c in secret_message)
    binary_message += '1111111111111110' 
    
    if len(binary_message) > len(audio.raw_data):
        raise ValueError("Message too long for this audio file")
    
    raw_data = bytearray(audio.raw_data)
    
    for i in range(len(binary_message)):
        byte = raw_data[i]
        new_byte = (byte & 0xFE) | int(binary_message[i])
        raw_data[i] = new_byte
    
    new_audio = audio._spawn(raw_data)
    new_audio.export(output_file, format="mp3")

hide_data_in_mp3("input.mp3", "output.mp3", "CodeVinciCTF{not_real_flag}")

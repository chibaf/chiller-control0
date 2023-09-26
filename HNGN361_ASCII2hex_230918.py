"""
{230917}
チラーから返信され戻ってくる運転状態（ポンプ単独運転）のバイト列（ワード）を再現する

マニュアルにあるページ数を忘れたんですけれども例題を、Pythonで再現してみます。

"""
response_J02 = b'\x02\x4A\x4F\x32\x03\x34'
STX=b'\x02'
J=b'\x4A'
O=b'\x4F'
data=b'\x32'  #数字の２
ETX=b'\x03'                           # bytes

integer_ETX=int.from_bytes(ETX, byteorder='big') 
print("integer_ETX=",integer_ETX)

s1="""
以下でBCCを計算しますが、演算子の ^ を使うと
integerどうしで XORが計算できて、以下の式で計算できます。
ちなみに、
ETXは、0x03 、です（上の式でプリントしてますが）。
"""
print(s1)

integer_BCC=ord('J')^ord('O')^ord('2')^0x03   # integer

print("type(ETX)=",type(ETX))
print("type(BCC), BCC=",type(integer_BCC), integer_BCC)

byte_BCC = integer_BCC.to_bytes((integer_BCC.bit_length() + 7) // 8, byteorder='big')
print("byte_BCC=",byte_BCC)

s1="""
これで、ひとそろい組み上げた bytes (バイト列)が完成します。
"""
answer_bytestring=STX+J+O+data+ETX+byte_BCC
print(s1, answer_bytestring)

s2="""
ちょっとみにくいので、全部をバイト表現にしてみました。
"""
hex_representation = ' '.join([f'{byte:02X}' for byte in answer_bytestring])
print(s2, hex_representation)

